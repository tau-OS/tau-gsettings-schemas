%global debug_package %{nil}

Name:           tau-gsettings-schemas
Version:        1.1
Release:        3%{?dist}
Summary:        tauOS specific GSettings schemas

License:        GPL
URL:            https://github.com/tau-OS/tau-gsettings-schemas
Source:         %{name}-%{version}.tar.gz

BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  gcc

%description
Global GSettings schemas for tauOS. That's all.

%prep
%autosetup

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
