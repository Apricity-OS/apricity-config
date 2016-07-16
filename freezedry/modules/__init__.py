from .pacman_module import PacmanModule
from .systemd_module import SystemdModule
from .vim_module import VimModule
from .gnome_module import GnomeModule
from .gdm_module import GdmModule
from .zsh_module import ZshModule
from .codeModule import CodeModule
from .core import ModulePool

reserved_words = ['inherits']

all_modules = {'pacman': PacmanModule,
               'systemd': SystemdModule,
               'vim': VimModule,
               'gnome': GnomeModule,
               'gdm': GdmModule,
               'zsh': ZshModule,
               'code': CodeModule}
