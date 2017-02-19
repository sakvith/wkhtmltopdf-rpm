Name:           wkhtmltopdf
Version:        0.12.4
Release:        1%{?dist}
Summary:        wkhtmltopdf

License:        GPL
URL:            http://wkhtmltopdf.org
Source0:        wkhtmltox-0.12.4_linux-generic-amd64.tar.xz

#BuildRequires:  
Requires:       libXrender, fontconfig, libXext, freetype

%description
Simple shell utility to convert html to pdf using the webkit rendering engine, and qt.

#Disable stripping of static binaries
%global __os_install_post %{nil}

%prep
%setup -c

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

#Create /usr/bin dir
install -m 755 -d $RPM_BUILD_ROOT/%{_bindir}

#Create /usr/lib dir
install -m 755 -d $RPM_BUILD_ROOT/%{_libdir}

#Create /usr/include dir
install -m 755 -d $RPM_BUILD_ROOT/%{_includedir}/wkhtmltox

#Create /usr/share/man dir
install -m 755 -d $RPM_BUILD_ROOT/%{_mandir}/man1


#Copy wkhtml binary 
install -m 775 wkhtmltox/bin/wkhtmltopdf $RPM_BUILD_ROOT%{_bindir}/wkhtmltopdf
install -m 775 wkhtmltox/bin/wkhtmltoimage $RPM_BUILD_ROOT%{_bindir}/wkhtmltoimage

#Copy lib
install -m 775 wkhtmltox/lib/libwkhtmltox.so $RPM_BUILD_ROOT%{_libdir}/libwkhtmltox.so
install -m 775 wkhtmltox/lib/libwkhtmltox.so.0 $RPM_BUILD_ROOT%{_libdir}/libwkhtmltox.so.0
install -m 775 wkhtmltox/lib/libwkhtmltox.so.0.12 $RPM_BUILD_ROOT%{_libdir}/libwkhtmltox.so.0.12
install -m 775 wkhtmltox/lib/libwkhtmltox.so.0.12.4 $RPM_BUILD_ROOT%{_libdir}/libwkhtmltox.so.0.12.4

#Copy wkhtml includes
install -m 775 wkhtmltox/include/wkhtmltox/dllbegin.inc $RPM_BUILD_ROOT%{_includedir}/wkhtmltox/dllbegin.inc
install -m 775 wkhtmltox/include/wkhtmltox/dllend.inc $RPM_BUILD_ROOT%{_includedir}/wkhtmltox/dllend.inc
install -m 775 wkhtmltox/include/wkhtmltox/image.h $RPM_BUILD_ROOT%{_includedir}/wkhtmltox/image.h
install -m 775 wkhtmltox/include/wkhtmltox/pdf.h $RPM_BUILD_ROOT%{_includedir}/wkhtmltox/pdf.h

#Copy wkhtml man
install -m 775 wkhtmltox/share/man/man1/wkhtmltopdf.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/wkhtmltopdf.1.gz
install -m 775 wkhtmltox/share/man/man1/wkhtmltoimage.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/wkhtmltoimage.1.gz


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/wkhtmltopdf
%{_bindir}/wkhtmltoimage
%{_libdir}/libwkhtmltox.so
%{_libdir}/libwkhtmltox.so.0
%{_libdir}/libwkhtmltox.so.0.12
%{_libdir}/libwkhtmltox.so.0.12.4
%{_includedir}/wkhtmltox/dllbegin.inc
%{_includedir}/wkhtmltox/dllend.inc
%{_includedir}/wkhtmltox/image.h
%{_includedir}/wkhtmltox/pdf.h
%{_mandir}/man1/wkhtmltopdf.1.gz
%{_mandir}/man1/wkhtmltoimage.1.gz


%changelog
*Sat Nov 18 2017 Sakvith Jayasinghe <devsakvith@gmail.com> 0.12.4-1
-Initial build 
