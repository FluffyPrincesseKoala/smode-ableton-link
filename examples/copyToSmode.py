isOn: Oil.Boolean(True)
isPlay: Oil.Boolean(True)
myReal: Oil.Real(25.4)

import sys
import asyncio
import smodeLink
import threading

# Add the path to the directory containing the compiled extension module
sys.path.append('F:/AbletonDev/smode-ableton-link/build/Release')

# Import your module as if it was installed in the standard library
import smodeLink

# Explicitly create a new event loop
loop = asyncio.new_event_loop()

link = smodeLink.Link(script.myReal.get(), loop)
link.enabled = script.isOn.get()
link.start_stop_sync_enabled = True
link.playing = script.isPlay.get()


async def run():
    while link.playing and script.isPlay.get():
        #script.myReal.set(link.tempo)
        link.tempo = script.myReal.get()
        print(link.enabled)
        if link.playing:
            beat = await link.sync(beat=1, offset=0, origin=0)
            print(f'Sync action at beat: {beat}')

def start_asyncio_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run())
    #asyncio.run(run())

# Create and start a new thread to run the asyncio event loop
loop_thread = threading.Thread(target=start_asyncio_loop, args=(loop,))
loop_thread.start()