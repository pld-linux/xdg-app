Summary:	Application deployment framework for desktop apps
Summary(pl.UTF-8):	Szkielet do wdrażania aplikacji desktopowych
Name:		xdg-app
Version:	0.3.6
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://www.freedesktop.org/software/xdg-app/releases/%{name}-%{version}.tar.xz
# Source0-md5:	3bc835b96b8f2d5652c45bb7d2ef7ade
URL:		https://wiki.gnome.org/Projects/SandboxedApps
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libgsystem-devel >= 2015.1
BuildRequires:	libseccomp-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libxslt-progs
BuildRequires:	ostree-devel >= 2015.3
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libgsystem >= 2015.1
Requires:	ostree >= 2015.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application deployment framework for desktop apps.

%description -l pl.UTF-8
Szkielet do wdrażania aplikacji desktopowych.

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
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/xdg-app
%attr(755,root,root) %{_bindir}/xdg-app-helper
%attr(755,root,root) %{_libexecdir}/xdg-app-session-helper
%attr(755,root,root) %{_libexecdir}/xdg-dbus-proxy
%attr(755,root,root) /etc/profile.d/xdg-app.sh
%{_datadir}/dbus-1/services/xdg-app-session.service
%{_datadir}/gdm/env.d/xdg-app.env
%{_datadir}/xdg-app
%{_mandir}/man1/xdg-app*.1*

%files -n bash-completion-xdg-app
%defattr(644,root,root,755)
%{_datadir}/bash-completion/completions/xdg-app
