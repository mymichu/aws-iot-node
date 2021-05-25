from conans import ConanFile
from conans import tools
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain
import os
version="2.5.2"

project_username = os.getenv("CONAN_USERNAME", "disroop")
project_channel = os.getenv("CONAN_CHANNEL", "development")


class Unity(ConanFile):
    name = "unity"
    url = "todo add url"
    version = f"{version}"
    channel = f"{project_channel}"
    user = f"{project_username}"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps","CMakeToolchain","virtualenv"
    description = "Pure C Testing Framework."
    exports_sources = "CMakeLists.txt", "FreeRTOSConfig.h"

    def generate(self):
        if self.settings.arch == "armv7":
            tc = CMakeToolchain(self)
            tc.variables["CMAKE_TRY_COMPILE_TARGET_TYPE"] = "STATIC_LIBRARY"
            tc.generate()

    def source(self):
        git=tools.Git(folder=self.source_folder)
        git.clone("https://github.com/ThrowTheSwitch/Unity.git", branch=f"v{version}", shallow=True)

    def package(self):
        self.copy("*.h", src="src", dst="include", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package_info(self):
        self.cpp_info.libs.append("unity")