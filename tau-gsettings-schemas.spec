%global debug_package %{nil}

Name:           tau-gsettings-schemas
Version:        1.1
Release:        7%{?dist}
Summary:        tauOS specific GSettings schemas

License:        GPL
URL:            https://github.com/tau-OS/tau-gsettings-schemas
Source:         https://github.com/tau-OS/tau-gsettings-schemas/archive/refs/heads/main.zip

BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  gcc

%description
Global GSettings schemas for tauOS. That's all.

%prep
%autosetup -n %{name}-main

%build
%meson
%meson_build

%install
%meson_install

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%license LICENSE
%{_datadir}/glib-2.0/schemas/*

%changelog
* Sun Oct 23 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 1.1-3
- Rebuilt
