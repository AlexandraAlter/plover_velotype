"""
    Some abbreviations are used in this source file:
      ic=initial consonants
      fc=final consonants
      v=vowels
      tv=thumb vowels
      sym=symbols
      acc=accented
"""

from dataclasses import dataclass

from plover.system import english_stenotype

# _ ZFSPTCKJR LN H ´ IOE 'UAY OIE ` NL KJRPTCFSZ

KEYS = (
    # shifts
    '#',
    # RHS heel
    '_-',
    # LHS consonants fingers
    'Z-', 'F-', 'S-', 'P-', 'T-', 'C-', 'K-', 'J-', 'R-',
    # LHS consonants thumb
    'L-', 'N-',
    # LHS heel
    'H-',
    # LHS thumb syms
    '´-',
    # LHS vowels fingers
    'I-', 'O-', 'E-',
    # Finger syms
    "'",
    # Shared vowels fingers
    'U', 'A',
    # Shared vowels thumb
    'Y',
    # RHS vowels fingers
    '-O', '-I', '-E',
    # RHS thumb syms
    '-`',
    # RHS consonants thumb
    '-N', '-L',
    # RHS consonants fingers
    '-K', '-J', '-R', '-P', '-T', '-C', '-F', '-S', '-Z',
)


@dataclass
class VeloGroup:
    """A convenience class for storing groups of keys that are looked up together"""
    meta: str
    keys: str
    lhs_only: bool = False
    rhs_only: bool = False

    def __add__(self, other):
        if not isinstance(other, VeloGroup):
            raise ValueError('Cannot add a VeloGroup to a non-Velogroup')
        keys = self.keys + other.keys
        rhs_only = self.rhs_only and other.rhs_only
        lhs_only = self.lhs_only and other.lhs_only
        return VeloGroup(self.meta + other.meta, keys, rhs_only, lhs_only)


# used in the Velotype Extension
# these MUST be in steno order because of assumptions made in the extension
# meta-strokes are used to define and protect split strokes from being picked up
# meta-strokes (+«<=>») must not be used to define regular strokes
PREFIX_G = VeloGroup('+', '_')
IC_G = VeloGroup('«', 'ZFSPTCKJRLNH', lhs_only=True)
ACC_V_G = VeloGroup('<=>', "´IOE-'UAYOIE`")
FC_G = VeloGroup('»', '-NLKJRPTCFSZ', rhs_only=True)

TV_G = VeloGroup('<', 'Y')
V_G = VeloGroup('=', 'IOE-UAOIE')
SYM_G = VeloGroup('>', "´'`")

L_COMB_G = IC_G + ACC_V_G
R_COMB_G = ACC_V_G + FC_G
ALL_G = IC_G + ACC_V_G + FC_G
# end of custom section

# this is intentionally restricted to hyphen-less keys
IMPLICIT_HYPHEN_KEYS = ("'", 'U', 'A', 'Y', '8', '5', '2', '0')

# this is intentionally left empty
SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'P-': '%-',
    'K-': '&-',
    'I-': '7-',
    "'": '8',
    '-O': '-9',
    '-K': '-?',
    '-P': '-!',

    'F-': '£-',
    'T-': 's-', # should be '/', but that is an invalid stroke
    'J-': '*-',
    'O-': '4-',
    'U': '5',
    '-I': '-6',
    '-J': '-e', # should be '=', but that is used as a meta character
    '-T': '-;',
    '-F': "-'",

    'Z-': '@-',
    'S-': '$-',
    'C-': '(-',
    'R-': 'p-', # should be '+', but that is used as a meta character
    'E-': '1-',
    'A': '2',
    '-E': '-3',
    '-R': '-d', # should be '-', but that is an invalid stroke
    '-C': '-)',
    '-S': '-:',
    '-Z': '-h', # should be '#', but that is already a stroke

    'L-': '€-',
    'N-': ',-',
    'Y': '0',
    '-N': '-.',
    '-L': '-u', # should be '_', but that is used by NoSpace

    '´-': '~-',
    '-`': '-¨',
}

UNDO_STROKE_STENO = 'SN-NS'

ORTHOGRAPHY_RULES = english_stenotype.ORTHOGRAPHY_RULES
ORTHOGRAPHY_RULES_ALIASES = english_stenotype.ORTHOGRAPHY_RULES_ALIASES

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        'P-': '3',
        'K-': '4',
        'I-': '5',
        "'":  '6',
        '-O': '7',
        '-K': '8',
        '-P': '9',

        'F-': 'w',
        'T-': 'e',
        'J-': 'r',
        'O-': 't',
        'U':  'y',
        '-I': 'u',
        '-J': 'i',
        '-T': 'o',
        '-F': 'p',

        'Z-': ('q', 'a'),
        'S-': 's',
        'C-': 'd',
        'R-': 'f',
        'E-': 'g',
        'A':  'h',
        '-E': 'j',
        '-R': 'k',
        '-C': 'l',
        '-S': ';',
        '-Z': ('[', "'"),

        'L-': 'v',
        'N-': 'b',
        'Y':  'n',
        '-N': 'm',
        '-L': ',',

        '´-': 'c',
        '#':  ('x', '/'),
        '-`': '.',

        '_-': 'space',
        'H-': 'z',

        'arpeggiate': 'Return',
        'no-op': ('`', '1', '2', '0', '-', '=', ']', '\\'),
    },

    'Gemini PR': {
        'P-': '#3',
        'K-': '#4',
        'I-': '#5',
        "'":  '#6',
        '-O': '#7',
        '-K': '#8',
        '-P': '#9',

        'F-': 'S1-',
        'T-': 'T-',
        'J-': 'P-',
        'O-': 'H-',
        'U':  '*1',
        '-I': '-F',
        '-J': '-P',
        '-T': '-L',
        '-F': '-T',

        'Z-': 'res2',
        'S-': 'S2-',
        'C-': 'K-',
        'R-': 'W-',
        'E-': 'R-',
        'A':  '*2',
        '-E': '-R',
        '-R': '-B',
        '-C': '-G',
        '-S': '-S',
        '-Z': '-Z',

        'L-': 'A-',
        'N-': 'O-',
        'Y':  'Fn',
        '-N': '-E',
        '-L': '-U',

        '´-': '*3',
        '#':  'res1',
        '-`': '*4',

        'H-': '#1',
        '_-': '-D',
    },
}

# Normally this kind of duplication would be handled using KEYMAP_MACHINE_TYPE,
#   but due to the way the keymap fallback is done, these layouts would lose their
#   extra keys, so this exists as a patch for that issue.
KEYMAPS['Gemini PR Footpedal'] = KEYMAPS['Gemini PR']
KEYMAPS['Keyboard Plus'] = KEYMAPS['Keyboard']

DICTIONARIES_ROOT = 'asset:plover_velotype:assets'
DEFAULT_DICTIONARIES = (
    'velo_user.json',
    'velo_commands.json',
    'velo_english_basic.json',
    'velo_base.json',
)

