set(SOURCES
${CMAKE_CURRENT_LIST_DIR}/free-rtos.c
${CMAKE_CURRENT_LIST_DIR}/stm32l4xx_hal_timebase_TIM.c
${CMAKE_CURRENT_LIST_DIR}/stm32l4xx_it.c
${CMAKE_CURRENT_LIST_DIR}/stm32l4xx_it.h
${CMAKE_CURRENT_LIST_DIR}/syscalls.c
${CMAKE_CURRENT_LIST_DIR}/system_stm32l4xx.c
)

add_Library(platform_obj OBJECT ${SOURCES})

find_package(stm32_bsp_iot_node REQUIRED)
find_package(freertos_kernel REQUIRED)

target_link_libraries(platform_obj PRIVATE stm32_bsp_iot_node::stm32_bsp_iot_node freertos_kernel::freertos_kernel)