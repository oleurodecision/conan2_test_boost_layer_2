# ============================================================================
# CMake configuration
# ============================================================================

cmake_minimum_required (VERSION 3.19)

# ============================================================================
# Project configuration
# ============================================================================

project (layer2
	VERSION 0.0
	LANGUAGES CXX)

# ============================================================================
# External requirements
# ============================================================================

# ----------------------------------------------------------------------------
# External requirements setup
# ----------------------------------------------------------------------------
# additional cmake modules
list (PREPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

# library behaviour
set (CMAKE_FIND_PACKAGE_SORT_ORDER NATURAL)
set (CMAKE_FIND_PACKAGE_SORT_DIRECTION DEC)
set (CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)

# ----------------------------------------------------------------------------
# Dependency version number
# ----------------------------------------------------------------------------
set (Layer2_BOOST_VERSION 1.75.0)

# ============================================================================
# Compiler configurations
# ============================================================================

# ----------------------------------------------------------------------------
# Compilation settings
# ----------------------------------------------------------------------------
set (CMAKE_CXX_STANDARD 14)
set (CMAKE_CXX_STANDARD_REQUIRED OFF)
set (CMAKE_CXX_EXTENSIONS OFF)

set (CMAKE_POSITION_INDEPENDENT_CODE ON)

# ----------------------------------------------------------------------------
# Default compilation flags
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Coverage build type definition
# ----------------------------------------------------------------------------
option (${PROJECT_NAME}_WITH_COVERAGE "enable coverage" OFF)
if (${PROJECT_NAME}_WITH_COVERAGE)
	include (Coverage)
endif ()

# ============================================================================
# Installation
# ============================================================================

include (GNUInstallDirs)

if (CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
	set (CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/install/${PROJECT_NAME}-${PROJECT_VERSION}" CACHE PATH "${PROJECT_NAME} default install path" FORCE)
endif ()

# ----------------------------------------------------------------------------
# Configuration files
# ----------------------------------------------------------------------------
set (ConfigPackageLocation "lib/cmake/${PROJECT_NAME}-${PROJECT_VERSION}")

include (CMakePackageConfigHelpers)

write_basic_package_version_file ("${CMAKE_CURRENT_BINARY_DIR}/cmake/${PROJECT_NAME}-config-version.cmake"
	VERSION ${PROJECT_VERSION}
	COMPATIBILITY SameMinorVersion
	)

configure_package_config_file (cmake/${PROJECT_NAME}-config.cmake.in
	"${CMAKE_CURRENT_BINARY_DIR}/cmake/${PROJECT_NAME}-config.cmake"
	INSTALL_DESTINATION "${ConfigPackageLocation}"
	NO_SET_AND_CHECK_MACRO
	NO_CHECK_REQUIRED_COMPONENTS_MACRO
	)

# ----------------------------------------------------------------------------
# Install
# ----------------------------------------------------------------------------
install (FILES
	"${CMAKE_CURRENT_BINARY_DIR}/cmake/${PROJECT_NAME}-config.cmake"
	"${CMAKE_CURRENT_BINARY_DIR}/cmake/${PROJECT_NAME}-config-version.cmake"
	DESTINATION "${ConfigPackageLocation}"
	)

# ============================================================================
# Targets configurations
# ============================================================================

add_subdirectory (src)
