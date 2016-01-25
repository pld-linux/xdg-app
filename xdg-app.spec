#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Application deployment framework for desktop apps
Summary(pl.UTF-8):	Szkielet do wdrażania aplikacji desktopowych
Name:		xdg-app
Version:	0.4.6
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://www.freedesktop.org/software/xdg-app/releases/%{name}-%{version}.tar.xz
# Source0-md5:	81e7f737c4575bf94da170d780bac492
URL:		https://wiki.gnome.org/Projects/SandboxedApps
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	glib2-devel >= 1:2.45.8
BuildRequires:	gobject-introspection-devel >= 1.40.0
BuildRequires:	gtk-doc >= 1.20
BuildRequires:	json-glib-devel >= 1.0
BuildRequires:	libarchive-devel >= 2.8.0
BuildRequires:	libfuse-devel
BuildRequires:	libgsystem-devel >= 2015.1
BuildRequires:	libseccomp-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libxslt-progs
BuildRequires:	ostree-devel >= 2015.6
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xz
Requires:	libgsystem >= 2015.1
Requires:	ostree >= 2015.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application deployment framework for desktop apps.

%description -l pl.UTF-8
Szkielet do wdrażania aplikacji desktopowych.

%package libs
Summary:	Shared xdg-app library
Summary(pl.UTF-8):	Biblioteka współdzielona xdg-app
Group:		Libraries
Requires:	glib2 >= 1:2.45.8
Requires:	libgsystem >= 2015.1
Requires:	ostree >= 2015.6

%description libs
Shared xdg-app library.

%description libs -l pl.UTF-8
Biblioteka współdzielona xdg-app.

%package devel
Summary:	Header files for xdg-app library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki xdg-app
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.45.8
Requires:	libgsystem-devel >= 2015.1
Requires:	ostree-devel >= 2015.6

%description devel
Header files for xdg-app library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki xdg-app.

%package static
Summary:	Static xdg-app library
Summary(pl.UTF-8):	Biblioteka statyczna xdg-app
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static xdg-app library.

%description static -l pl.UTF-8
Biblioteka statyczna xdg-app.

%package apidocs
Summary:	API documentation for xdg-app library
Summary(pl.UTF-8):	Dokumentacja API biblioteki xdg-app
Group:		Documentation

%description apidocs
API documentation for xdg-app library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki xdg-app.

%package -n bash-completion-xdg-app
Summary:	Bash completion for xdg-app command
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów polecenia xdg-app
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2

%description -n bash-completion-xdg-app
Bash completion for xdg-app command.

%description -n bash-completion-xdg-app -l pl.UTF-8
Bashowe uzupełnianie parametrów polecenia xdg-app.

%prep
%setup -q

%build
%configure \
	--enable-libxdgapp \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxdg-app.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/xdg-app
%attr(755,root,root) %{_bindir}/xdg-app-builder
%attr(755,root,root) %{_bindir}/xdg-app-helper
%attr(755,root,root) %{_libexecdir}/xdg-app-session-helper
%attr(755,root,root) %{_libexecdir}/xdg-dbus-proxy
%attr(755,root,root) %{_libexecdir}/xdg-document-portal
%attr(755,root,root) /etc/profile.d/xdg-app.sh
%{_datadir}/dbus-1/interfaces/org.freedesktop.XdgApp.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Documents.xml
%{_datadir}/dbus-1/services/xdg-app-session.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Documents.service
# not supported by PLD gdm (yet?)
#%{_datadir}/gdm/env.d/xdg-app.env
%{_datadir}/xdg-app
%{_mandir}/man1/xdg-app*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxdg-app.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxdg-app.so.0
%{_libdir}/girepository-1.0/XdgApp-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxdg-app.so
%{_includedir}/xdg-app
%{_datadir}/gir-1.0/XdgApp-1.0.gir
%{_pkgconfigdir}/xdg-app.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxdg-app.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/xdg-app

%files -n bash-completion-xdg-app
%defattr(644,root,root,755)
%{_datadir}/bash-completion/completions/xdg-app
