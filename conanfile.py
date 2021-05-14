from conans import ConanFile
from conans import tools
from conan.tools.cmake import CMake, CMakeDeps
import os



class AwsIotNode(ConanFile):
    name = "aws_iot_node"
    version = "0.1.0"
    license = "closed"
    url = "TODO"
    default_channel = "development"
    default_user = "mymichu"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps","CMakeToolchain","cmake_vars","virtualenv"
    exports_sources = "src/*", "CMakeLists.txt","linker"
    
    def requirements(self):
        self.requires(f"stm32_bsp_iot_node/1.1.7@disroop/development")
        self.requires(f"cmake_vars/1.0.0@disroop/development",private=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
    