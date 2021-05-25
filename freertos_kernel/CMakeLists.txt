cmake_minimum_required(VERSION 3.16)
#Include Conan
include(${CMAKE_CURRENT_BINARY_DIR}/cmake_vars.cmake)
include(${CMAKE_CURRENT_BINARY_DIR}/conan_toolchain.cmake)
project(FREERTOS_KERNEL C)

set(CMAKE_C_STANDARD 99)

find_package(unity REQUIRED)

set(LIBRARY_NAME free_rtos_kernel)
set(SOURCES 
${CMAKE_CURRENT_LIST_DIR}/tasks.c
${CMAKE_CURRENT_LIST_DIR}/queue.c
${CMAKE_CURRENT_LIST_DIR}/list.c
${CMAKE_CURRENT_LIST_DIR}/timers.c
${CMAKE_CURRENT_LIST_DIR}/stream_buffer.c
${CMAKE_CURRENT_LIST_DIR}/croutine.c
${CMAKE_CURRENT_LIST_DIR}/event_groups.c
${CMAKE_CURRENT_LIST_DIR}/portable/Common/mpu_wrappers.c
${CMAKE_CURRENT_LIST_DIR}/portable/GCC/ARM_CM4F/port.c
${CMAKE_CURRENT_LIST_DIR}/portable/MemMang/heap_1.c
${CMAKE_CURRENT_LIST_DIR}/portable/MemMang/heap_2.c
${CMAKE_CURRENT_LIST_DIR}/portable/MemMang/heap_3.c
${CMAKE_CURRENT_LIST_DIR}/portable/MemMang/heap_4.c
${CMAKE_CURRENT_LIST_DIR}/portable/MemMang/heap_5.c)

add_library(${LIBRARY_NAME} STATIC ${SOURCES})
target_include_directories(${LIBRARY_NAME} PUBLIC ${CMAKE_CURRENT_LIST_DIR} ${CMAKE_CURRENT_LIST_DIR}/include ${CMAKE_CURRENT_LIST_DIR}/portable/GCC/ARM_CM4F)
target_link_libraries(${LIBRARY_NAME} STATIC unity::unity)