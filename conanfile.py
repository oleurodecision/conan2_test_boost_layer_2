import os
import re

from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import load, update_conandata
from conan.tools.scm import Git

from inspect import getsourcefile

class Layer2Conan(ConanFile):
    # package reference
    name, version = "layer2", "0.0"

    # metadata
    description = "conan2_test_boost_layer2"
    license = "MIT"
    author = "Olivier Liess"
    homepage = "https://github.com/oleurodecision/conan2_test_boost_layer2"

    # binary model
    package_type = "header-library"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False]
    }
    default_options = {
        "shared": False,
        "fPIC": True
        }

    no_copy_source = True

    #def init(self):

    #def set_name(self):

    #def set_version(self):

    def export(self):
        git = Git(self, self.recipe_folder)
        scm_url, scm_commit = git.get_url_and_commit()
        update_conandata(self, {"sources": {"commit": scm_commit, "url": scm_url}})

    #def export_sources(self):

    # init is called again when doing some conan create .

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    #def configure(self):

    def layout(self):
        build_dir = os.path.join("builds", str(self.settings.os), str(self.settings.compiler), str(self.settings.compiler.version), str(self.settings.arch), str(self.settings.build_type))
        cmake_config_path = os.path.join("lib", "cmake", f"{self.name}-{self.version}")

        # set folders
        self.folders.build = build_dir
        self.folders.generators = os.path.join(build_dir, "generators")

        # set cpp package information for package consumption
        self.cpp.package.builddirs = [cmake_config_path]

        # set cpp source and build information for editable consumption
        self.cpp.build.builddirs = [os.path.join("install", cmake_config_path)]

    def requirements(self):
        self.requires("layer1/0.0")

    #def package_id(self):

    def validate(self):
        check_min_cppstd(self, "14")

    #def validate_build(self):

    #def build_requirements(self):

    #def build_id(self):

    def source(self):
        git = Git(self)
        sources = self.conan_data["sources"]
        git.clone(url=sources["url"], target=".")
        git.checkout(commit=sources["commit"])

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    # removed ?
    #def imports(self):
    #    self.copy("*.dll", dst="bin", src="bin")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")

    # undefined order

    #def system_requirements(self):

    #def compatibility(self):

    #def deploy(self):

