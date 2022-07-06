Name:           tau-gsettings-schemas
Version:        1.1
Release:        1%{?dist}
Summary:        tauOS specific GSettings schemas

License:        GPL
URL:            https://github.com/tau-OS/tau-gsettings-schemas
Source:         %{name}-%{version}.tar.gz

BuildRequires:  glib2-devel
BuildRequires:  meson

%prep
%autosetup -c

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
{_datadir}/glib-2.0/schemas/*
