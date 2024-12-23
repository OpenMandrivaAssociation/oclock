Summary:	Round X clock
Name:		oclock
Version:	1.0.6
Release:	1
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xmu) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xt) >= 1.0.0

%description
Oclock simply displays the current time on an analog display.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/oclock
%{_datadir}/X11/app-defaults/Clock-color
%doc %{_mandir}/man1/oclock.*
