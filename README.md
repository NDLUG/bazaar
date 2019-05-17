# bazaar
Tool to help install common programs for new Linux users

# LUG Distro (lugOS)

### Platforms

We wish to support:

1. **x86_64** : Laptops and Desktops
2. **armv7l** : Raspberry Pi 2+

### Environments

We wish to have a **live** and **installable** version of each of the following environments:

1. **Casual** : A **Budgie** or **GNOME** based desktop environment for casual or novice users.
2. **Hacker** : An **i3wm** + **XFCE4** based environment for power users.


### Debate: Snaps vs. Flatpaks

| Snaps  | Flatpaks|
|:------|:------|
| Included with Ubuntu 18.04+ | Must be installed from repos and FlatHub must be added |
| Backed by Canonical | Backed by Torvalds | 
| Not visually appealing | Respects your DE |
| *snapd* runs in background, auto-updating apps whenever possible, eating CPU cycles | FlatPaks update like any other normal package manager |
| Does no play nice with SELinux (if we decide to use this | ... also has raised security concerns in the past |

### Should we always include *build-essential*?

**Pros**
- Automatically includes almost all the tools needed for most of the department classes

**Cons**
- Must be installed later
- Takes extra disk space, may be an issue for Raspberry Pi users

## Debate: Native when possible or Snap/Flatpak when possible?

*flame war goes here*

## Layers

There are meta-packages and scripts geared toward specific use cases:

1. **Courses**

* Introduction to Engineering
  * Easy MATLAB instructions
  * FileZilla
  * LibreSuite (Excel needed...)
* Principles of Computing
* Elements of Computing
* Fundamentals of Computing
* Data Structures
* Systems Programming
* Programming Paradigms
* Operating Systems
* Databases
* VFX

2. **Notre Dame Specific Software**

* Printing
  * Current print drivers for Linux not functioning
  * There is a [solution written in Python 2.7](https://github.com/junaidali/pharos-linux), which is not usable, however maybe we can learn from it 
* Wireless
  * Eduroam drivers, the provided ones also outdated (we think)
  * Cisco AnyConnect VPN Profile - see [vpn.sh](https://github.com/NDLUG/bazaar/blob/master/vpn.sh)
* Two-Factor Authentication
  * Something with Okta?
  
3. **Activity**
* Gaming
  * Steam
  * Lutris
  * PlayOnLinux
  * WineStaging?
* Web Development
  * VueJS / React
  * VSCode / Atom
* Android Development
  * Android Studio + ADB Drivers
* Media Production
  * Kdenlive vs. DaVinci Resolve
  * Audacity
  * OBS Studio
* Graphics
  * AMD Drivers
  * NVidia Drivers
* Casual Use
  * Slack
  * Chrome/Firefox/insert another browser here
  * Discord
  * Spotify
  * Etcher
  * Telegram
  * Signal
  * WhatsApp
  * Clients for OneDrive / DropBox / Google Drive ?
  * Skype ?
  
## Utilities

1. Welcome screen / software outique similar to Ubuntu Mate
2. Installer
