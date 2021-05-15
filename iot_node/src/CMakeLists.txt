set(APP_NAME test)

set(SOURCES
${CMAKE_CURRENT_LIST_DIR}/main.c
${CMAKE_CURRENT_LIST_DIR}/main.h
${CMAKE_CURRENT_LIST_DIR}/stm32l4xx_it.c
${CMAKE_CURRENT_LIST_DIR}/stm32l4xx_it.h
${CMAKE_CURRENT_LIST_DIR}/system_stm32l4xx.c
)

find_package(stm32_bsp_iot_node REQUIRED)
find_package(stm32_runtime_l475 REQUIRED)

set(LINKER_SCRIPT ${CMAKE_CURRENT_LIST_DIR}/linker/STM32L475VGTx_FLASH.ld)

add_executable(${APP_NAME} ${SOURCES})
target_link_libraries(${APP_NAME} PRIVATE stm32_bsp_iot_node::stm32_bsp_iot_node stm32_runtime_l475::stm32_runtime_l475)
#set_target_properties(${TARGET_NAME} PROPERTIES LINK_DEPENDS ${LINKER_SCRIPT})
target_link_options(${APP_NAME} PRIVATE -T ${LINKER_SCRIPT} -Xlinker -Map=${APP_NAME}.map)

#target_link_options(${APP_NAME} PRIVATE -Xlinker -Map=${APP_NAME}.map LINKER:-whole-archive ${stm32_runtime_l475_LIB_DIRS_DEBUG}/libstm32_runtime_l475.a LINKER:-no-whole-archive)