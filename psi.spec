%define name	psi
%define version	0.12
%define release	%mkrel 0.Rc2.1
%define section	Internet/Instant Messaging
%define title	PSI
%define Summary	PSI Jabber client using QT4

# TODO
# repackage iconsets and language files as noarch

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Networking/Instant messaging
URL:		http://psi-im.org
Source0:	http://prdownloads.sourceforge.net/psi/%name-%version-RC2.tar.bz2
Source1:	%name-icons.tar.bz2
Source2:	%name-smileysets.tar.bz2
Source3:	%name-iconsets.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	qt4-devel 
BuildRequires:  openssl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libjingle-devel
Buildconflicts: qca2-devel
Requires:	%name-lang-pack

# to update, run:
# for i in de el es eo fi fr hu nl pl pt_BR sk sl vi bg mk;do wget http://psi-im.org/files/translation/%version/psi_${i}.qm -O `rpm --eval %_sourcedir`/psi_${i}.qm && bzip2 -f `rpm --eval %_sourcedir`/psi_${i}.qm;done
# Language packs
Source50:	psi_pl.qm.bz2
Source51:	psi_sr.qm.bz2
Source52:	psi_fr.qm.bz2
Source53:	psi_eo.qm.bz2
Source54:	psi_sr@Latn.qm.bz2
Source55:	psi_fi.qm.bz2
Source56:	psi_cs.qm.bz2
Source57:	psi_ru.qm.bz2
Source58:	psi_de.qm.bz2
Source59:	psi_es.qm.bz2
Source60:	psi_mk.qm.bz2
Source61:	psi_nl.qm.bz2
Source62:	psi_sk.qm.bz2
Source63:	psi_el.qm.bz2
Source64:	psi_it.qm.bz2
Source65:	psi_se.qm.bz2
Source66:	psi_zh.qm.bz2
Source67:	psi_et.qm.bz2
Source68:	psi_vi.qm.bz2
Source69:	psi_ca.qm.bz2
Source70:	psi_hu.qm.bz2
Source71:	psi_pt.qm.bz2
Source72:	psi_pt_BR.qm.bz2
Source73:	psi_sl.qm.bz2
Source74:	psi_bg.qm.bz2

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

%package -n %name-iconsets
Summary:	Package with iconsets
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}

%description -n %name-iconsets
This package contain a various iconsets for psi.

%package -n %name-smileysets
Summary:	Package with smileysets
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}

%description -n %name-smileysets
This package contain a various smileysets for psi.

%package -n %name-lang-pack-pl
Summary:	Poland language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-pl
Provides:	%name-lang-pack

%description -n %name-lang-pack-pl
This package adds support for pl to psi.

%package -n %name-lang-pack-sr
Summary:	Serbian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-sr
Provides:	%name-lang-pack

%description -n %name-lang-pack-sr
This package adds support for sr to psi.

%package -n %name-lang-pack-fr
Summary:	France language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-fr
Provides:	%name-lang-pack

%description -n %name-lang-pack-fr
This package adds support for fr to psi.

%package -n %name-lang-pack-eo
Summary:	Esperanto language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-eo
Provides:	%name-lang-pack

%description -n %name-lang-pack-eo
This package adds support for eo to psi.

%package -n %name-lang-pack-sr_lat
Summary:	Serbian latin language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-sr
Provides:	%name-lang-pack

%description -n %name-lang-pack-sr_lat
This package adds support for sr_lat to psi.

%package -n %name-lang-pack-fi
Summary:	Finland language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-fi
Provides:	%name-lang-pack

%description -n %name-lang-pack-fi
This package adds support for fi to psi.

%package -n %name-lang-pack-cs
Summary:	Czech language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-cs
Provides:	%name-lang-pack

%description -n %name-lang-pack-cs
This package adds support for cs to psi.

%package -n %name-lang-pack-ru
Summary:	Russian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-ru
Provides:	%name-lang-pack

%description -n %name-lang-pack-ru
This package adds support for ru to psi.

%package -n %name-lang-pack-de
Summary:	Deutsch language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-de
Provides:	%name-lang-pack

%description -n %name-lang-pack-de
This package adds support for de to psi.

%package -n %name-lang-pack-es
Summary:	Spanish language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-es
Provides:	%name-lang-pack

%description -n %name-lang-pack-es
This package adds support for es to psi.

%package -n %name-lang-pack-mk
Summary:	Macedonia language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-mk
Provides:	%name-lang-pack

%description -n %name-lang-pack-mk
This package adds support for mk to psi.

%package -n %name-lang-pack-nl
Summary:	Dutch language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-nl
Provides:	%name-lang-pack

%description -n %name-lang-pack-nl
This package adds support for nl to psi.

%package -n %name-lang-pack-sk
Summary:	Slovak language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-sk
Provides:	%name-lang-pack

%description -n %name-lang-pack-sk
This package adds support for sk to psi.

%package -n %name-lang-pack-el
Summary:	Greek language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-el
Provides:	%name-lang-pack

%description -n %name-lang-pack-el
This package adds support for el to psi.

%package -n %name-lang-pack-it
Summary:	Italy language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-it
Provides:	%name-lang-pack

%description -n %name-lang-pack-it
This package adds support for it to psi.

%package -n %name-lang-pack-se
Summary:	Svedish language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-se
Provides:	%name-lang-pack

%description -n %name-lang-pack-se
This package adds support for se to psi.

%package -n %name-lang-pack-zh
Summary:	Chinese language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-zh
Provides:	%name-lang-pack

%description -n %name-lang-pack-zh
This package adds support for zh to psi.

%package -n %name-lang-pack-et
Summary:	Estonian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-et
Provides:	%name-lang-pack

%description -n %name-lang-pack-et
This package adds support for et to psi.

%package -n %name-lang-pack-vi
Summary:	Vietnamese language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-vi
Provides:	%name-lang-pack

%description -n %name-lang-pack-vi
This package adds support for vi to psi.

%package -n %name-lang-pack-ca
Summary:	Catalanian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-ca
Provides:	%name-lang-pack

%description -n %name-lang-pack-ca
This package adds support for ca to psi.

%package -n %name-lang-pack-hu
Summary:	Hungarian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-hu
Provides:	%name-lang-pack

%description -n %name-lang-pack-hu
This package adds support for hu to psi.

%package -n %name-lang-pack-pt
Summary:	Partugal language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-pt
Provides:	%name-lang-pack

%description -n %name-lang-pack-pt
This package adds support for pt to psi.

%package -n %name-lang-pack-pt_br
Summary:	Portugal brazilian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-pt
Provides:	%name-lang-pack

%description -n %name-lang-pack-pt_br
This package adds support for pt_br to psi.

%package -n %name-lang-pack-sl
Summary:	Slovenian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-sl
Provides:	%name-lang-pack

%description -n %name-lang-pack-sl
This package adds support for sl to psi.

%package -n %name-lang-pack-bg
Summary:	Bulgarian language pack for psi
Group:		Networking/Instant messaging
Requires:	locales-bg
Provides:	%name-lang-pack

%description -n %name-lang-pack-bg
This package adds support for bg to psi.

%package -n %name-lang-pack-en
Summary:        English language pack for psi
Group:          Networking/Instant messaging
Requires:       locales-en
Provides:       %name-lang-pack

%description -n %name-lang-pack-en
This package adds support for en to psi.

%prep
%setup -q  -n %name-%version-RC2
%setup -q -T -D -a1 -a2 -a3  -n %name-%version-RC2

%build

export QTDIR=/usr/lib/qt4/
./configure --prefix=%{_prefix}  --bindir=%{_bindir}  --datadir=%{_datadir} --enable-debug 
%make

%install
rm -rf %{buildroot}
INSTALL_ROOT=%{buildroot}
export INSTALL_ROOT
%makeinstall_std

# if some set is added/removed don't remember update files section too
# Install smileysets
%__cp %{name}-smileysets/* %{buildroot}%{_datadir}/%name/iconsets/emoticons
# Install iconsets
%__cp %{name}-iconsets/* %{buildroot}%{_datadir}/%name/iconsets/system

# Install language packages
%__bzip2 -dc %{SOURCE50} > %{buildroot}%{_datadir}/%name/%{name}_pl.qm
%__bzip2 -dc %{SOURCE51} > %{buildroot}%{_datadir}/%name/%{name}_sr.qm
%__bzip2 -dc %{SOURCE52} > %{buildroot}%{_datadir}/%name/%{name}_fr.qm
%__bzip2 -dc %{SOURCE53} > %{buildroot}%{_datadir}/%name/%{name}_eo.qm
%__bzip2 -dc %{SOURCE54} > %{buildroot}%{_datadir}/%name/%{name}_sr@Latn.qm
%__bzip2 -dc %{SOURCE55} > %{buildroot}%{_datadir}/%name/%{name}_fi.qm
%__bzip2 -dc %{SOURCE56} > %{buildroot}%{_datadir}/%name/%{name}_cs.qm
%__bzip2 -dc %{SOURCE57} > %{buildroot}%{_datadir}/%name/%{name}_ru.qm
%__bzip2 -dc %{SOURCE58} > %{buildroot}%{_datadir}/%name/%{name}_de.qm
%__bzip2 -dc %{SOURCE59} > %{buildroot}%{_datadir}/%name/%{name}_es.qm
%__bzip2 -dc %{SOURCE60} > %{buildroot}%{_datadir}/%name/%{name}_mk.qm
%__bzip2 -dc %{SOURCE61} > %{buildroot}%{_datadir}/%name/%{name}_nl.qm
%__bzip2 -dc %{SOURCE62} > %{buildroot}%{_datadir}/%name/%{name}_sk.qm
%__bzip2 -dc %{SOURCE63} > %{buildroot}%{_datadir}/%name/%{name}_el.qm
%__bzip2 -dc %{SOURCE64} > %{buildroot}%{_datadir}/%name/%{name}_it.qm
%__bzip2 -dc %{SOURCE65} > %{buildroot}%{_datadir}/%name/%{name}_se.qm
%__bzip2 -dc %{SOURCE66} > %{buildroot}%{_datadir}/%name/%{name}_zh.qm
%__bzip2 -dc %{SOURCE67} > %{buildroot}%{_datadir}/%name/%{name}_et.qm
%__bzip2 -dc %{SOURCE68} > %{buildroot}%{_datadir}/%name/%{name}_vi.qm
%__bzip2 -dc %{SOURCE69} > %{buildroot}%{_datadir}/%name/%{name}_ca.qm
%__bzip2 -dc %{SOURCE70} > %{buildroot}%{_datadir}/%name/%{name}_hu.qm
%__bzip2 -dc %{SOURCE71} > %{buildroot}%{_datadir}/%name/%{name}_pt.qm
%__bzip2 -dc %{SOURCE72} > %{buildroot}%{_datadir}/%name/%{name}_pt_BR.qm
%__bzip2 -dc %{SOURCE73} > %{buildroot}%{_datadir}/%name/%{name}_sl.qm
%__bzip2 -dc %{SOURCE74} > %{buildroot}%{_datadir}/%name/%{name}_bg.qm


# Menu
desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-Internet-InstantMessaging" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*



# icons
%__install -D -m 644 %{name}48.png %buildroot/%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot/%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot/%_miconsdir/%name.png

%clean
rm -rf %{buildroot}

%files 
%defattr(0755,root,root,0755)
%{_bindir}/*
%defattr(0644,root,root,0755)
%doc README COPYING
%exclude %{_datadir}/%name/README
%exclude %{_datadir}/%name/COPYING
%dir %{_datadir}/%{name}
# certs
%dir %{_datadir}/%{name}/certs
%{_datadir}/%{name}/certs/*
# iconsets
%dir %{_datadir}/%{name}/iconsets
%dir %{_datadir}/%{name}/iconsets/system
%dir %{_datadir}/%{name}/iconsets/system/default
# system
%{_datadir}/%{name}/iconsets/system/README
#%{_datadir}/%{name}/iconsets/system/crystal_system.jisp
%{_datadir}/%{name}/iconsets/system/default/*
# roster
%dir %{_datadir}/%{name}/iconsets/roster
%{_datadir}/%{name}/iconsets/roster/*
# emoticons
%dir %{_datadir}/%{name}/iconsets/emoticons
%dir %{_datadir}/%{name}/iconsets/emoticons/default
%{_datadir}/%{name}/iconsets/emoticons/default/*
# sound
%dir %{_datadir}/%{name}/sound
%{_datadir}/%{name}/sound/*
# menu and icons
%{_datadir}/applications/psi.desktop
%_miconsdir/*
%_iconsdir/*
%_liconsdir/*

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

%files -n %name-lang-pack-pl
%defattr(-,root,root)
%{_datadir}/%name/%{name}_pl.qm

%files -n %name-lang-pack-sr
%defattr(-,root,root)
%{_datadir}/%name/%{name}_sr.qm

%files -n %name-lang-pack-fr
%defattr(-,root,root)
%{_datadir}/%name/%{name}_fr.qm

%files -n %name-lang-pack-eo
%defattr(-,root,root)
%{_datadir}/%name/%{name}_eo.qm

%files -n %name-lang-pack-sr_lat
%defattr(-,root,root)
%{_datadir}/%name/%{name}_sr@Latn.qm

%files -n %name-lang-pack-fi
%defattr(-,root,root)
%{_datadir}/%name/%{name}_fi.qm

%files -n %name-lang-pack-cs
%defattr(-,root,root)
%{_datadir}/%name/%{name}_cs.qm

%files -n %name-lang-pack-ru
%defattr(-,root,root)
%{_datadir}/%name/%{name}_ru.qm

%files -n %name-lang-pack-de
%defattr(-,root,root)
%{_datadir}/%name/%{name}_de.qm

%files -n %name-lang-pack-es
%defattr(-,root,root)
%{_datadir}/%name/%{name}_es.qm

%files -n %name-lang-pack-mk
%defattr(-,root,root)
%{_datadir}/%name/%{name}_mk.qm

%files -n %name-lang-pack-nl
%defattr(-,root,root)
%{_datadir}/%name/%{name}_nl.qm

%files -n %name-lang-pack-sk
%defattr(-,root,root)
%{_datadir}/%name/%{name}_sk.qm

%files -n %name-lang-pack-el
%defattr(-,root,root)
%{_datadir}/%name/%{name}_el.qm

%files -n %name-lang-pack-it
%defattr(-,root,root)
%{_datadir}/%name/%{name}_it.qm

%files -n %name-lang-pack-se
%defattr(-,root,root)
%{_datadir}/%name/%{name}_se.qm

%files -n %name-lang-pack-zh
%defattr(-,root,root)
%{_datadir}/%name/%{name}_zh.qm

%files -n %name-lang-pack-et
%defattr(-,root,root)
%{_datadir}/%name/%{name}_et.qm

%files -n %name-lang-pack-vi
%defattr(-,root,root)
%{_datadir}/%name/%{name}_vi.qm

%files -n %name-lang-pack-ca
%defattr(-,root,root)
%{_datadir}/%name/%{name}_ca.qm

%files -n %name-lang-pack-hu
%defattr(-,root,root)
%{_datadir}/%name/%{name}_hu.qm

%files -n %name-lang-pack-pt
%defattr(-,root,root)
%{_datadir}/%name/%{name}_pt.qm

%files -n %name-lang-pack-pt_br
%defattr(-,root,root)
%{_datadir}/%name/%{name}_pt_BR.qm

%files -n %name-lang-pack-sl
%defattr(-,root,root)
%{_datadir}/%name/%{name}_sl.qm

%files -n %name-lang-pack-bg
%defattr(-,root,root)
%{_datadir}/%name/%{name}_bg.qm

%files -n %name-lang-pack-en
%defattr(-,root,root)


