cmake_minimum_required(VERSION 3.16)

project(smodeLink)

# Set policy CMP0148 to NEW
cmake_policy(SET CMP0148 NEW)

# Set build type to Release if not specified
if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

# Use C++20 standard
set(CMAKE_CXX_STANDARD 20)

# Manually set Python paths
# set(Python_EXECUTABLE "C:/Users/jerry/AppData/Local/Microsoft/WindowsApps/python3.12.exe")
set(Python_EXECUTABLE "F:/Smode Community/python/python.exe")
# set(Python_INCLUDE_DIRS "C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.12_3.12.1264.0_x64__qbz5n2kfra8p0/include")
set(Python_INCLUDE_DIRS "F:/Smode Community/python/DLLS/oui") # had to install missing python headers from site-packages
# set(Python_LIBRARIES "C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.12_3.12.1264.0_x64__qbz5n2kfra8p0/libs/python312.lib")
set(Python_LIBRARIES "F:/Smode Community/python/Libs")

# Pass these variables to CMake
set(Python3_EXECUTABLE ${Python_EXECUTABLE})
set(Python3_INCLUDE_DIR ${Python_INCLUDE_DIRS})
set(Python3_LIBRARY ${Python_LIBRARIES})

# Find Python libraries and include directories
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# Set PYBIND11_FINDPYTHON ON before including pybind11
set(PYBIND11_FINDPYTHON ON CACHE BOOL "")

# Add pybind11 subdirectory
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/ext/pybind11)

# Create the Python module
pybind11_add_module(smodeLink src/aalink.cpp)

# Include Python directories
target_include_directories(smodeLink PRIVATE ${Python_INCLUDE_DIRS})

# Link against Python libraries
target_link_libraries(smodeLink PRIVATE ${Python_LIBRARIES})

# Include Ableton Link configuration and link libraries
include(${CMAKE_CURRENT_SOURCE_DIR}/ext/link/AbletonLinkConfig.cmake)
target_link_libraries(smodeLink PUBLIC Ableton::Link)

# Install the DLL to the current directory
install(TARGETS smodeLink LIBRARY DESTINATION .)
