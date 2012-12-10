%define srcname kde_cdemu
%define version 0.4

Name:		kde-cdemu-manager
Version:	%version
Release:	%mkrel 1
Summary:	A simple front-end for CDemu
Source0:	http://kde-apps.org/CONTENT/content-files/99752-%{srcname}-%{version}.tar.bz2
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://kde-apps.org/content/show.php/KDE+CDEmu+Manager?content=99752
BuildRequires:	kdelibs4-devel
Requires:	cdemu-client >= 1.2.0

%description
KDE CDemu Manager is a simple front-end for CDemu.

It provides a little manager window that gives you an overview of your virtual
drives and allows you to mount and unmount images.

It also includes a KDE service menu for mounting images directly from
Dolphin/Konqueror (which is what most people will want to use).

Images can be unmounted like any other media through Dolphin or the Device
Notifier widget.

%files -f %srcname.lang
%defattr(-,root,root)
%{_kde_bindir}/kde_cdemu
%{_kde_applicationsdir}/kde_cdemu.desktop
%{_kde_appsdir}/kde_cdemu/kde_cdemuui.rc
%{_kde_services}/ServiceMenus/kde_cdemu_mount.desktop

%prep
%setup -q -n %{srcname}
find . -name '*.cpp' -exec chmod 644 {} \;
find . -name '*.h' -exec chmod 644 {} \;

%build
%cmake_kde4

%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %{srcname}


%changelog
* Mon Feb 27 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.4-1mdv2011.0
+ Revision: 781131
- update to 0.4

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-3mdv2011.0
+ Revision: 612555
- the mass rebuild of 2010.1 packages

* Fri Dec 11 2009 Ahmad Samir <ahmadsamir@mandriva.org> 0.3-2mdv2010.1
+ Revision: 476570
- require cdemu >= 1.2.0

* Sat Dec 05 2009 Ahmad Samir <ahmadsamir@mandriva.org> 0.3-1mdv2010.1
+ Revision: 473643
- Add patch for servicemenu .desktop file to make it
  compliant with XDG standards
- import kde-cdemu-manager


