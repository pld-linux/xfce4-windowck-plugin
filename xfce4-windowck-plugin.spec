Summary:	Xfce panel plugin which allows to put the maximized window title and windows buttons on the panel
Name:		xfce4-windowck-plugin
Version:	0.6.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-windowck-plugin/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	e721212f27223b73f2d305be9a71b02a
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-windowck-plugin
BuildRequires:	glib2-devel >= 1:2.64.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 3.22
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.16.0
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	xfce-preferred-applications >= 4.16.0
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
BuildRequires:	xfconf-devel >= 4.16.0
Requires:	xfce4-panel >= 4.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce panel plugin which allows to put the maximized window title and
windows buttons on the panel.

It's main features are:

- Show the title and buttons of the maximized window on the panel.
- Allow window actions on buttons and title clicks (activate,
  (un)maximize, close).
- Allow window action menu on left button click.
- Title formatting options.
- xfwm4/unity theming support for buttons.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# unsupported locale
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,ru_RU}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwckbuttons.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwckmenu.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwcktitle.so
%{_datadir}/xfce4/panel/plugins/wckbuttons.desktop
%{_datadir}/xfce4/panel/plugins/wckmenu.desktop
%{_datadir}/xfce4/panel/plugins/wcktitle.desktop
%{_iconsdir}/hicolor/*x*/apps/wckbuttons-plugin.png
%{_iconsdir}/hicolor/*x*/apps/wckmenu-plugin.png
%{_iconsdir}/hicolor/*x*/apps/wcktitle-plugin.png
%{_datadir}/themes/Windowck
%{_datadir}/themes/Windowck-dark
