add_executable(tinygpt_runtime
    src/main.cpp
)

target_include_directories(tinygpt_runtime
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)
