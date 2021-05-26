set(APP_NAME test)

add_subdirectory(platform)

set(SOURCES
${CMAKE_CURRENT_LIST_DIR}/main.c
)

find_package(stm32_bsp_iot_node REQUIRED)
find_package(stm32_runtime_l475_vtg REQUIRED)
find_package(freertos_kernel REQUIRED)

add_executable(${APP_NAME} ${SOURCES} $<TARGET_OBJECTS:platform_obj>)
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
