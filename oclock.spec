Name: oclock
Version: 1.0.3
Release: 1
Summary: Round X clock
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: pkgconfig(xkbfile)
BuildRequires: x11-util-macros >= 1.0.1

%description
Oclock simply displays the current time on an analog display.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/oclock
%{_datadir}/X11/app-defaults/Clock-color
%{_mandir}/man1/oclock.*




%changelog
* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.3-1
+ Revision: 781035
- BR:pkgconfig(xkbfile)
- version update 1.0.3

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2
+ Revision: 666939
- mass rebuild

* Thu Sep 23 2010 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 580691
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-9mdv2010.1
+ Revision: 523460
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-8mdv2010.0
+ Revision: 426266
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-7mdv2009.1
+ Revision: 351645
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 223357
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 166410
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-4mdv2008.1
+ Revision: 156489
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2008.0
+ Revision: 67339
- fix man pages extension

