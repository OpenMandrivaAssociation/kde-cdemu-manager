%define srcname kde_cdemu
%define version 0.3

Name:		kde-cdemu-manager
Version:	%version
Release:	%mkrel 1
Summary:	A simple front-end for CDemu
Source0:	http://kde-apps.org/CONTENT/content-files/99752-%{srcname}-%{version}.tar.gz
Patch1:		kde-cdemu-manager-0.3-servicemenu.patch
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://kde-apps.org/content/show.php/KDE+CDEmu+Manager?content=99752
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	kdelibs4-devel
Requires:	cdemu-client

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
%setup -q -n %{srcname}-%{version}
%patch1 -p1 -b .servicemenu

%build
%cmake_kde4

%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %{srcname}

%clean
%__rm -rf %{buildroot}
