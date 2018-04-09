Summary:	Round X clock
Name:		oclock
Version:	1.0.4
Release:	1
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xmu) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xt) >= 1.0.0

%description
Oclock simply displays the current time on an analog display.

%prep
%setup -q

%build
%configure2_5x \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/oclock
%{_datadir}/X11/app-defaults/Clock-color
%{_mandir}/man1/oclock.*

