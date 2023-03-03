# ============================================================================
# External requirements
# ============================================================================

#----------------------------------------------------------------------------
# Threads
#----------------------------------------------------------------------------
find_package (Threads REQUIRED)

# ----------------------------------------------------------------------------
# Boost
# ----------------------------------------------------------------------------
find_package (layer1 0.0 REQUIRED)

# ============================================================================
# Targets configuration
# ============================================================================

configure_file (${PROJECT_SOURCE_DIR}/cmake/layer2Version.hh.in ${CMAKE_CURRENT_BINARY_DIR}/layer2Version.hh)

# ----------------------------------------------------------------------------
# library (common) configuration
# ----------------------------------------------------------------------------
add_library (layer2 INTERFACE)

set_target_properties (layer2
	PROPERTIES
		OUTPUT_NAME layer2-${PROJECT_VERSION}
		VERSION ${PROJECT_VERSION}
		SOVERSION ${PROJECT_MAJOR}.${PROJECT_MINOR}
	)

target_include_directories (layer2
	INTERFACE
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
	)

target_link_libraries (layer2
	INTERFACE
		layer1::layer1	
	)

# ============================================================================
# Install configuration
# ============================================================================

install (TARGETS layer2 EXPORT layer2-export
	INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install (DIRECTORY src/layer2
	DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
	FILES_MATCHING PATTERN "*.hh"
)

install (FILES ${CMAKE_CURRENT_BINARY_DIR}/layer2Version.hh
	DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
	)

install (EXPORT layer2-export
	FILE ${PROJECT_NAME}-targets.cmake
	NAMESPACE ${PROJECT_NAME}::
	DESTINATION "${ConfigPackageLocation}"
	)

# ----------------------------------------------------------------------------
# Export configuration
# ----------------------------------------------------------------------------
add_library (${PROJECT_NAME}::layer2 ALIAS layer2)

