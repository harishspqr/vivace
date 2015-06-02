Summary:	Netwide Assembler.
Name:		nasm
Version:	2.11.08
Release:	1
License:	BSD
URL:		http://www.nasm.us
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.xz
#BuildRequires:	pkg-config util-macros libX11-devel libXext-devel
#Requires:	libX11 libXext
%description
NASM (Netwide Assembler) is an 80x86 assembler designed for portability and modularity. It includes a disassembler as well. 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make INSTALLROOT=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 2.11.08-1
-	initial version