Name: oclock
Version: 1.0.1
Release: %mkrel 4
Summary: Round X clock
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libx11-devel	>= 1.1.3
BuildRequires: libxext-devel	>= 1.0.3
BuildRequires: libxmu-devel	>= 1.0.4
BuildRequires: libxt-devel	>= 1.0.5

%description
Oclock simply displays the current time on an analog display.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/oclock
%{_datadir}/X11/app-defaults/Clock-color
%{_mandir}/man1/oclock.*


