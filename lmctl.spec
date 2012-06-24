Summary:	lmctl - configuration tool for Logitech USB Mice
Summary(pl):	lmctl - narz�dzie konfiguracyjne dla myszy USB Logitech
Name:		lmctl
Version:	0.3.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.bedroomlan.org/~alexios/files/SOFTWARE/lmctl/%{name}_%{version}.tar.gz
# Source0-md5:	c2acb088c95adeac68b6de8f05ddc0e4
URL:		http://www.bedroomlan.org/~alexios/coding_lmctl.html
BuildRequires:	libusb-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lmctl can enable and disable the special features on recent Logitech
mice (if they're connected to a USB port). Features like wireless
status reporting, battery charge indication, resolution and
SmartScroll can be controlled this way.

%description -l pl
lmctl potrafi w��cza� i wy��cza� specjalne mo�liwo�ci nowych myszy
Logitech (je�li s� pod��czone do portu USB). Mo�na w ten spos�b
sterowa� mo�liwo�ciami takimi jak bezprzewodowe zg�aszanie stanu,
wska�nik �adowania baterii, rozdzielczo�� czy SmartScroll.

%prep
%setup -q -n %{name}-0.3.1

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -D__USE_GNU"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README debian/changelog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/lmctl*
