set(APP_NAME test)

set(SOURCES
${CMAKE_CURRENT_LIST_DIR}/main.c
${CMAKE_CURRENT_LIST_DIR}/stm32l4xx_it.c
${CMAKE_CURRENT_LIST_DIR}/stm32l4xx_it.h
${CMAKE_CURRENT_LIST_DIR}/system_stm32l4xx.c
${CMAKE_CURRENT_LIST_DIR}/syscalls.c
${CMAKE_CURRENT_LIST_DIR}/stm32l4xx_hal_timebase_TIM.c
)

find_package(stm32_bsp_iot_node REQUIRED)
find_package(stm32_runtime_l475_vtg REQUIRED)
find_package(freertos_kernel REQUIRED)

set(LINKER_SCRIPT ${CMAKE_CURRENT_LIST_DIR}/linker/STM32L475VGTx_FLASH.ld)

add_executable(${APP_NAME} ${SOURCES})
target_link_libraries(${APP_NAME} PRIVATE stm32_bsp_iot_node::stm32_bsp_iot_node stm32_runtime_l475_vtg::stm32_runtime_l475_vtg freertos_kernel::freertos_kernel)

set_target_properties(${APP_NAME}
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

find_package(Platform REQUIRED)
target_setup_runtime(${APP_NAME})
