Summary:	Xfce panel plugin which allows to put the maximized window title and windows buttons on the panel
Name:		xfce4-windowck-plugin
Version:	0.4.6
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	https://github.com/cedl38/xfce4-windowck-plugin/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a9d711a5ea0d3e7947e1fb4d4724e481
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-windowck-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
BuildRequires:	xfce-preferred-applications
Requires:	xfce4-panel >= 4.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce panel plugin which allows to put the maximized window title and
windows buttons on the panel.

It's main features are:

- Show the title and buttons of the maximized window on the panel.
- Allow window actions on buttons and title clicks (activate, (un)maximize, close).
- Allow window action menu on left button click.
- Title formatting options.
- xfwm4/unity theming support for buttons.

%prep
%setup -q

%build
./autogen.sh

%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwckbuttons.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwindowck.so
%{_datadir}/xfce4/panel/plugins/wckbuttons.desktop
%{_datadir}/xfce4/panel/plugins/windowck-plugin.desktop
%{_iconsdir}/hicolor/*x*/apps/wckbuttons-plugin.png
%{_iconsdir}/hicolor/*x*/apps/windowck-plugin.png
%{_datadir}/themes/Windowck
%{_datadir}/themes/Windowck-dark
