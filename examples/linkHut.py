# core modules
import asyncio
# import aalink # ../aalink.cpp compiled using pybind11
import sys

# Add the path to the directory containing the compiled extension module
sys.path.append('../build/Debug')

# Now you can import your module as if it was installed in the standard library
import aalink

# CLI modules
import keyboard
import aioconsole

class LinkHut:
    def __init__(self):
        self.loop = asyncio.get_event_loop()  # Get the current asyncio event loop
        self.link = aalink.Link(120.0, self.loop)  # Initialize with a tempo of 120 BPM and the current event loop
        self.link.enabled = False  # Enable Link by default
        self.running = True
        self.refresh_rate = 0.1  # Refresh rate in seconds for the status update
        self.playing_task = None

    def printStatus(self):
        isEnabled = "Enabled" if self.link.enabled else "Disabled"
        currentTempo = self.link.tempo
        currentQuantum = self.link.quantum
        isSyncing = "Syncing" if self.link.start_stop_sync_enabled else "Not Syncing"
        connectedPeers = self.link.num_peers

        print("\033[H\033[J")# clear the screen
        print(f"Link Status: {isEnabled} (space = Toggle Link Enabled/Disabled)")
        print(f"Tempo: {currentTempo} BPM (w/e = +/- 1 BPM)")
        print(f"Quantum: {currentQuantum} (r/t = +/- 1 Quantum)")
        print(f"Sync Status: {isSyncing} (s = Toggle Start/Stop Sync)")
        print(f"Playing: {self.link.playing} (p = Toggle Play/Stop)")
        print(f"Connected Peers: {connectedPeers}")
        print("q - Quit")


    def setup_keyboard_listeners(self):
        keyboard.add_hotkey('m', lambda: self.quit())
        keyboard.add_hotkey(' ', lambda: self.toggle_link_enabled())
        keyboard.add_hotkey('w', lambda: self.adjust_tempo(1))
        keyboard.add_hotkey('e', lambda: self.adjust_tempo(-1))
        keyboard.add_hotkey('r', lambda: self.adjust_quantum(1))
        keyboard.add_hotkey('t', lambda: self.adjust_quantum(-1))
        keyboard.add_hotkey('s', lambda: self.toggle_sync())
        keyboard.add_hotkey('p', lambda: self.toggle_play())

    async def run(self):
        self.setup_keyboard_listeners()
        while self.running:
            self.printStatus()
            if self.link.playing:
                beat = await self.link.sync(beat=1, offset=0, origin=0)
                print(f'Sync action at beat: {beat}')
            await asyncio.sleep(self.refresh_rate)

    def toggle_link_enabled(self):
        self.link.enabled = not self.link.enabled

    async def sync_action(self, interval):
        """Perform an action in sync with the Link session."""
        while self.link.playing:
            beat = await self.link.sync(interval)
            print(f'Sync action at beat: {beat}')

    def toggle_play(self):
        self.link.playing = not self.link.playing
        if self.link.playing:
            if not hasattr(self, 'playing_task') or self.playing_task is None or self.playing_task.done():
                # Schedule the coroutine in the event loop from a non-async context
                asyncio.run_coroutine_threadsafe(self.sync_action(1), self.loop)
            else:
                self.playing_task.cancel()
                # Optionally handle cancellation
        else:
            if self.playing_task and not self.playing_task.done():
                self.playing_task.cancel()
        
    def toggle_sync(self):
        self.link.start_stop_sync_enabled = not self.link.start_stop_sync_enabled

    def adjust_tempo(self, delta):
        self.link.tempo += delta

    def adjust_quantum(self, delta):
        self.link.quantum += delta

    def quit(self):
        self.running = False
        print("Exiting...")
        keyboard.unhook_all()

async def main():
    cli = LinkHut()
    await cli.run()

if __name__ == "__main__":
    asyncio.run(main())
