%define name	psi
%define version	0.14
%define release	%mkrel	4
%define section	Internet/Instant Messaging
%define title	PSI
%define Summary	Jabber client using QT4

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://psi-im.org
Source0:	http://prdownloads.sourceforge.net/psi/%name-%version.tar.bz2
Source1:	%name-icons.tar.bz2
Source2:	%name-smileysets.tar.bz2
Source3:	%name-iconsets.tar.bz2
Patch1:		psi-0.14-rc1-qca.patch
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	qt4-devel 
BuildRequires:	openssl-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libjingle-devel
BuildRequires:	aspell-devel
BuildRequires:	enchant-devel
BuildRequires:	qca2-devel
Requires:	%name-lang-pack = %{version}-%{release}
Requires:	qca2-plugin-openssl
Suggests:	qca2-plugin-gnupg
Suggests:	psi-plugin-media
#Obsoletes old translations from 0.9.3
Obsoletes:	psi-lang-pack-fi < 0.14-2
Obsoletes:	psi-lang-pack-eo < 0.14-2
Obsoletes:	psi-lang-pack-se < 0.14-2
Obsoletes:	psi-lang-pack-hu < 0.14-2
Obsoletes:	psi-lang-pack-sk < 0.14-2
Obsoletes:	psi-lang-pack-vi < 0.14-2
Obsoletes:	psi-lang-pack-el < 0.14-2
Obsoletes:	psi-lang-pack-sr < 0.14-2
Obsoletes:	psi-lang-pack-et < 0.14-2
Obsoletes:	psi-lang-pack-nl < 0.14-2
Obsoletes:	psi-lang-pack-bg < 0.14-2
Obsoletes:	psi-lang-pack-pt < 0.14-2
Obsoletes:	psi-lang-pack-ca < 0.14-2
Obsoletes:	psi-lang-pack-sr_lat < 0.14-2

#Translations files has been moved on psi website, you can update them using this little script
#For the main psi translation
#for i in be cs de es fr it ja mk pl pt_BR ru sl sv ur_PK zh_TW ;do wget http://psi-im.org/download/lang/psi_${i}.qm && bzip2 -f psi_${i}.qm;done

Source50:	psi_pl.qm.bz2
Source51:	psi_fr.qm.bz2
Source52:	psi_cs.qm.bz2
Source53:	psi_ru.qm.bz2
Source54:	psi_de.qm.bz2
Source55:	psi_es.qm.bz2
Source56:	psi_mk.qm.bz2
Source57:	psi_it.qm.bz2
Source58:	psi_zh_TW.qm.bz2
Source59:	psi_pt_BR.qm.bz2
Source60:	psi_sl.qm.bz2
Source61:	psi_be.qm.bz2
Source62:	psi_ur_PK.qm.bz2
Source63:	psi_ja.qm.bz2
Source64:	psi_sv.qm.bz2

#Additional Qt translations
#for i in pl fr ru de es mk be ur_PK sv; do wget http://psi-im.org/download/lang/qt_${i}.qm && bzip2 -f qt_${i}.qm;done

Source70:	qt_pl.qm.bz2
Source71:	qt_fr.qm.bz2
Source73:	qt_ru.qm.bz2
Source74:	qt_de.qm.bz2
Source75:	qt_es.qm.bz2
Source76:	qt_mk.qm.bz2
Source81:	qt_be.qm.bz2
Source82:	qt_ur_PK.qm.bz2
Source84:	qt_sv.qm.bz2


%description
Psi is the premiere Instant Messaging application designed for Microsoft
Windows, Apple Mac OS X and GNU/Linux. Built upon an open protocol named
Jabber, Psi is a fast and lightweight messaging client that utilises the best
in open source technologies.
The goal of the Psi project is to create a powerful, yet easy-to-use
Jabber/XMPP client that tries to strictly adhere to the XMPP drafts.and Jabber
JEPs. This means that in most cases, Psi will not implement a feature unless
there is an accepted standard for it in the Jabber community. Doing so ensures
that Psi will be compatible, stable, and predictable, both from an end-user and
developer standpoint.

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/certs/README
%{_datadir}/%{name}/certs/startcom_ca.crt
%{_datadir}/%{name}/certs/startcom_ca_new.crt
%{_datadir}/%{name}/iconsets/emoticons/default/
%{_datadir}/%{name}/iconsets/roster/README
%{_datadir}/%{name}/iconsets/roster/*.jisp
%{_datadir}/%{name}/iconsets/roster/default/
%{_datadir}/%{name}/iconsets/system/README
%{_datadir}/%{name}/iconsets/system/default/
%{_datadir}/%{name}/sound/
%exclude %{_datadir}/%name/README
%exclude %{_datadir}/%name/COPYING

#--------------------------------------------------------------------

%package -n %name-iconsets
Summary:	Package with iconsets
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}

%description -n %name-iconsets
This package contain a various iconsets for psi.

%files -n %name-iconsets
%defattr(0644,root,root,0755)
%{_datadir}/%{name}/iconsets/system/amibulb.jisp
%{_datadir}/%{name}/iconsets/system/amiglobe.jisp
%{_datadir}/%{name}/iconsets/system/berlin-icq.jisp
%{_datadir}/%{name}/iconsets/system/berlin.jisp
%{_datadir}/%{name}/iconsets/system/chrome.jisp
%{_datadir}/%{name}/iconsets/system/dudes.jisp
%{_datadir}/%{name}/iconsets/system/dudes2.jisp
%{_datadir}/%{name}/iconsets/system/email.jisp
%{_datadir}/%{name}/iconsets/system/gothRoster.jisp
%{_datadir}/%{name}/iconsets/system/individual.jisp
%{_datadir}/%{name}/iconsets/system/kitty.jisp
%{_datadir}/%{name}/iconsets/system/lightbulb.jisp
%{_datadir}/%{name}/iconsets/system/msn6.jisp
%{_datadir}/%{name}/iconsets/system/neos.jisp
%{_datadir}/%{name}/iconsets/system/speechbubbles.jisp
%{_datadir}/%{name}/iconsets/system/stellar.jisp

#--------------------------------------------------------------------

%package -n %name-smileysets
Summary:	Package with smileysets
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}

%description -n %name-smileysets
This package contain a various smileysets for psi.

%files -n %name-smileysets
%defattr(0644,root,root,0755)
%{_datadir}/%{name}/iconsets/emoticons/AIM.jisp
%{_datadir}/%{name}/iconsets/emoticons/Chibi.jisp
%{_datadir}/%{name}/iconsets/emoticons/JIM.jisp
%{_datadir}/%{name}/iconsets/emoticons/KMess-Cartoon-1.0.jisp
%{_datadir}/%{name}/iconsets/emoticons/Ninja.jisp
%{_datadir}/%{name}/iconsets/emoticons/Taryn.jisp
%{_datadir}/%{name}/iconsets/emoticons/apple_ichat-1.0.jisp
%{_datadir}/%{name}/iconsets/emoticons/critters-1.0.jisp
%{_datadir}/%{name}/iconsets/emoticons/gadu-gadu.jisp
%{_datadir}/%{name}/iconsets/emoticons/icq-2002a.jisp
%{_datadir}/%{name}/iconsets/emoticons/ikonboard-3.1.jisp
%{_datadir}/%{name}/iconsets/emoticons/invision_board-1.0.1.jisp
%{_datadir}/%{name}/iconsets/emoticons/kreativ_squareheads.jisp
%{_datadir}/%{name}/iconsets/emoticons/megapack-1.0.jisp
%{_datadir}/%{name}/iconsets/emoticons/msn.jisp
%{_datadir}/%{name}/iconsets/emoticons/patricks_faces-1.0.jisp
%{_datadir}/%{name}/iconsets/emoticons/shinyicons.jisp
%{_datadir}/%{name}/iconsets/emoticons/tlen.pl-3.73.jisp
%{_datadir}/%{name}/iconsets/emoticons/trill-basic-smileys.jisp
%{_datadir}/%{name}/iconsets/emoticons/webmessenger.jisp
%{_datadir}/%{name}/iconsets/emoticons/wpkontakt-2.4.1.jisp
%{_datadir}/%{name}/iconsets/emoticons/yahoo_messenger.jisp

#--------------------------------------------------------------------

%package -n %name-lang-pack-pl
Summary:	Poland language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-pl
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-pl
This package adds support for pl to psi.

%files -n %name-lang-pack-pl
%defattr(-,root,root)
%{_datadir}/%name/%{name}_pl.qm
%{_datadir}/%name/qt_pl.qm


#--------------------------------------------------------------------

%package -n %name-lang-pack-fr
Summary:	France language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-fr
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-fr
This package adds support for fr to psi.

%files -n %name-lang-pack-fr
%defattr(-,root,root)
%{_datadir}/%name/%{name}_fr.qm
%{_datadir}/%name/qt_fr.qm

#--------------------------------------------------------------------

%package -n %name-lang-pack-cs
Summary:	Czech language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-cs
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-cs
This package adds support for cs to psi.

%files -n %name-lang-pack-cs
%defattr(-,root,root)
%{_datadir}/%name/%{name}_cs.qm

#--------------------------------------------------------------------

%package -n %name-lang-pack-ru
Summary:	Russian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-ru
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-ru
This package adds support for ru to psi.

%files -n %name-lang-pack-ru
%defattr(-,root,root)
%{_datadir}/%name/%{name}_ru.qm
%{_datadir}/%name/qt_ru.qm

#--------------------------------------------------------------------

%package -n %name-lang-pack-de
Summary:	Deutsch language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-de
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-de
This package adds support for de to psi.

%files -n %name-lang-pack-de
%defattr(-,root,root)
%{_datadir}/%name/%{name}_de.qm
%{_datadir}/%name/qt_de.qm

#--------------------------------------------------------------------

%package -n %name-lang-pack-es
Summary:	Spanish language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-es
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-es
This package adds support for es to psi.

%files -n %name-lang-pack-es
%defattr(-,root,root)
%{_datadir}/%name/%{name}_es.qm
%{_datadir}/%name/qt_es.qm

#--------------------------------------------------------------------


%package -n %name-lang-pack-mk
Summary:	Macedonia language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-mk
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-mk
This package adds support for mk to psi.

%files -n %name-lang-pack-mk
%defattr(-,root,root)
%{_datadir}/%name/%{name}_mk.qm
%{_datadir}/%name/qt_mk.qm
%{_datadir}/%name/qt_mk.qm

#--------------------------------------------------------------------

%package -n %name-lang-pack-it
Summary:	Italy language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-it
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-it
This package adds support for it to psi.

%files -n %name-lang-pack-it
%defattr(-,root,root)
%{_datadir}/%name/%{name}_it.qm


#--------------------------------------------------------------------

%package -n %name-lang-pack-zh
Summary:	Chinese language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-zh
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-zh
This package adds support for zh to psi.

%files -n %name-lang-pack-zh
%defattr(-,root,root)
%{_datadir}/%name/%{name}_zh_TW.qm

#--------------------------------------------------------------------

%package -n %name-lang-pack-pt_br
Summary:	Portugal brazilian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-pt
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-pt_br
This package adds support for pt_br to psi.

%files -n %name-lang-pack-pt_br
%defattr(-,root,root)
%{_datadir}/%name/%{name}_pt_BR.qm

#--------------------------------------------------------------------

%package -n %name-lang-pack-sl
Summary:	Slovenian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-sl
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-sl
This package adds support for sl to psi.

%files -n %name-lang-pack-sl
%defattr(-,root,root)
%{_datadir}/%name/%{name}_sl.qm

#--------------------------------------------------------------------

%package -n %name-lang-pack-en
Summary:	English language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-en
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-en
This package adds support for en to psi.

%files -n %name-lang-pack-en
%defattr(-,root,root)

#--------------------------------------------------------------------

%package -n %name-lang-pack-be
Summary:	Belarusian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-be
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-be
This package adds support for be to psi.

%files -n %name-lang-pack-be
%defattr(-,root,root)
%{_datadir}/%name/%{name}_be.qm
%{_datadir}/%name/qt_be.qm

#--------------------------------------------------------------------

%package -n %name-lang-pack-ur_PK
Summary:	Urdu language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-ur
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-ur_PK
This package adds support for ur to psi.

%files -n %name-lang-pack-ur_PK
%defattr(-,root,root)
%{_datadir}/%name/%{name}_ur_PK.qm
%{_datadir}/%name/qt_ur_PK.qm

#--------------------------------------------------------------------

%package -n %name-lang-pack-ja
Summary:	Japanase language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-ja
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-ja
This package adds support for ja to psi.

%files -n %name-lang-pack-ja
%defattr(-,root,root)
%{_datadir}/%name/%{name}_ja.qm

#--------------------------------------------------------------------

%package -n %name-lang-pack-sv
Summary:	Swedish language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-sv
Provides:	%name-lang-pack = %{version}-%{release}

%description -n %name-lang-pack-sv
This package adds support for sv to psi.

%files -n %name-lang-pack-sv
%defattr(-,root,root)
%{_datadir}/%name/%{name}_sv.qm
%{_datadir}/%name/qt_sv.qm

#--------------------------------------------------------------------


%prep
%setup -q  -n %name-%version
%setup -q -T -D -a1 -a2 -a3  -n %name-%version
%patch1 -p0 -b .qca

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --datadir=%{_datadir} --libdir=%{_libdir} --disable-bundled-qca --no-separate-debug-info
%qmake_qt4 psi.pro

%make

%install
%__rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

# if some set is added/removed don't remember update files section too
# Install smileysets
%__cp %{name}-smileysets/* %{buildroot}%{_datadir}/%name/iconsets/emoticons
# Install iconsets
%__cp %{name}-iconsets/* %{buildroot}%{_datadir}/%name/iconsets/system

# Install language packages
%__bzip2 -dc %{SOURCE50} > %{buildroot}%{_datadir}/%name/%{name}_pl.qm
%__bzip2 -dc %{SOURCE51} > %{buildroot}%{_datadir}/%name/%{name}_fr.qm
%__bzip2 -dc %{SOURCE52} > %{buildroot}%{_datadir}/%name/%{name}_cs.qm
%__bzip2 -dc %{SOURCE53} > %{buildroot}%{_datadir}/%name/%{name}_ru.qm
%__bzip2 -dc %{SOURCE54} > %{buildroot}%{_datadir}/%name/%{name}_de.qm
%__bzip2 -dc %{SOURCE55} > %{buildroot}%{_datadir}/%name/%{name}_es.qm
%__bzip2 -dc %{SOURCE56} > %{buildroot}%{_datadir}/%name/%{name}_mk.qm
%__bzip2 -dc %{SOURCE57} > %{buildroot}%{_datadir}/%name/%{name}_it.qm
%__bzip2 -dc %{SOURCE58} > %{buildroot}%{_datadir}/%name/%{name}_zh_TW.qm
%__bzip2 -dc %{SOURCE59} > %{buildroot}%{_datadir}/%name/%{name}_pt_BR.qm
%__bzip2 -dc %{SOURCE60} > %{buildroot}%{_datadir}/%name/%{name}_sl.qm
%__bzip2 -dc %{SOURCE61} > %{buildroot}%{_datadir}/%name/%{name}_be.qm
%__bzip2 -dc %{SOURCE62} > %{buildroot}%{_datadir}/%name/%{name}_ur_PK.qm
%__bzip2 -dc %{SOURCE63} > %{buildroot}%{_datadir}/%name/%{name}_ja.qm
%__bzip2 -dc %{SOURCE64} > %{buildroot}%{_datadir}/%name/%{name}_sv.qm

%__bzip2 -dc %{SOURCE70} > %{buildroot}%{_datadir}/%name/qt_pl.qm
%__bzip2 -dc %{SOURCE71} > %{buildroot}%{_datadir}/%name/qt_fr.qm
%__bzip2 -dc %{SOURCE73} > %{buildroot}%{_datadir}/%name/qt_ru.qm
%__bzip2 -dc %{SOURCE74} > %{buildroot}%{_datadir}/%name/qt_de.qm
%__bzip2 -dc %{SOURCE75} > %{buildroot}%{_datadir}/%name/qt_es.qm
%__bzip2 -dc %{SOURCE76} > %{buildroot}%{_datadir}/%name/qt_mk.qm
%__bzip2 -dc %{SOURCE81} > %{buildroot}%{_datadir}/%name/qt_be.qm
%__bzip2 -dc %{SOURCE82} > %{buildroot}%{_datadir}/%name/qt_ur_PK.qm
%__bzip2 -dc %{SOURCE84} > %{buildroot}%{_datadir}/%name/qt_sv.qm


# icons
%__install -D -m 644 %{name}48.png %buildroot/%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot/%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot/%_miconsdir/%name.png

%clean
%__rm -rf %{buildroot}
