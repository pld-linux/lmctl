Summary:	lmctl - configuration tool for Logitech USB Mice
Summary(pl.UTF-8):   lmctl - narzędzie konfiguracyjne dla myszy USB Logitech
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

%description -l pl.UTF-8
lmctl potrafi włączać i wyłączać specjalne możliwości nowych myszy
Logitech (jeśli są podłączone do portu USB). Można w ten sposób
sterować możliwościami takimi jak bezprzewodowe zgłaszanie stanu,
wskaźnik ładowania baterii, rozdzielczość czy SmartScroll.

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
