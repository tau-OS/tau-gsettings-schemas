project(
  'tau-gsettings-schemas', 'c',
  version: '1.1',
  license: 'GPL',
)

gnome = import('gnome')

settings_schemas = [ 'com.fyralabs.desktop.appearance.gschema.xml' ]
gnome.compile_schemas(depend_files: files(settings_schemas))

schemas_dir = get_option('prefix') / get_option('datadir') / 'glib-2.0' / 'schemas'
install_data(settings_schemas, install_dir: schemas_dir)

meson.add_install_script('glib-compile-schemas', schemas_dir)