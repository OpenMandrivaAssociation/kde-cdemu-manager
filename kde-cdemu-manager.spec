%define srcname kde_cdemu

Summary:	A simple KDE front-end for CDemu
Name:		kde-cdemu-manager
Version:	0.5.0
Release:	2
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://kde-apps.org/content/show.php/KDE+CDEmu+Manager?content=99752
Source0:	http://kde-apps.org/CONTENT/content-files/99752-%{srcname}-%{version}.tar.gz
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

%files -f %{srcname}.lang
%{_kde_bindir}/kde_cdemu
%{_kde_applicationsdir}/kde_cdemu.desktop
%{_kde_appsdir}/kde_cdemu/kde_cdemuui.rc
%{_kde_services}/ServiceMenus/kde_cdemu_mount.desktop

#----------------------------------------------------------------------------

%prep
%setup -q -n %{srcname}
find . -name '*.cpp' -exec chmod 644 {} \;
find . -name '*.h' -exec chmod 644 {} \;

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{srcname}

