Summary:	A date and time plugin for the Xfce panel
Name:		xfce4-windowck-plugin
Version:	0.3.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://github.com/cedl38/xfce4-windowck-plugin/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	88e0dea73ed5d6597af86432fcfb4f1c
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-windowck-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	xfce4-dev-tools >= 4.11.0
BuildRequires:	xfce4-panel-devel >= 4.11.0
Requires:	xfce4-panel >= 4.11.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An additional clock for the Xfce panel which also shows the date, with
adjustable font.

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
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwckbuttons.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwindowck.so
%{_datadir}/xfce4/panel/plugins/wckbuttons.desktop
%{_datadir}/xfce4/panel/plugins/windowck-plugin.desktop
%{_iconsdir}/hicolor/*x*/apps/wckbuttons-plugin.png
%{_iconsdir}/hicolor/*x*/apps/windowck-plugin.png
%{_datadir}/themes/Windowck
