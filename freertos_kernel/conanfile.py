from conans import ConanFile
from conans import tools
from conan.tools.cmake import CMake, CMakeDeps
import os
version="10.4.3"

project_username = os.getenv("CONAN_USERNAME", "disroop")
project_channel = os.getenv("CONAN_CHANNEL", "development")


class FreertosKernel(ConanFile):
    name = "freertos_kernel"
    url = "todo add url"
    version = f"{version}"
    channel = f"{project_channel}"
    user = f"{project_username}"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps","CMakeToolchain","cmake_vars","virtualenv"
    description = "Rtos for realtime system - only Kernel"
    exports_sources = "CMakeLists.txt", "FreeRTOSConfig.h"

    def requirements(self):
        self.requires(f"cmake_vars/1.0.0@disroop/development",private=True)
        self.requires(f"unity/2.5.2@disroop/development")

    def source(self):
        git=tools.Git(folder=self.source_folder)
        git.clone("https://github.com/FreeRTOS/FreeRTOS-Kernel.git", branch=f"V{version}", shallow=True)

    def package(self):
        self.copy("FreeRTOSConfig.h", dst="include", keep_path=False)
        self.copy("*.h", src="include", dst="include", keep_path=False)
        self.copy("*.h", src="portable/GCC/ARM_CM4F", dst="include", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package_info(self):
        self.cpp_info.libs.append("free_rtos_kernel")