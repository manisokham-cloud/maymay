"""
MAYMAY - Jeu Tetris en Python 3.12
Dépendance : pip install pygame
Lancement  : python maymay.py
"""

import pygame
import random
import sys
import base64
import io

# ── Photo de Maymay (base64) ────────────────────────────────────────────────
MAYMAY_ICON_B64 = "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RaC1kEy5MCdpEcCN7l68hEVrTcpS6iJppNJpILyUFLxWifPUMlLI8gurbmFpRh+ef+mjzzz78re+9c1nX3ltO7UpeHzjxt2f/vD86cm1a9ePMH/1b3zuC5//xP6VKyyVYKl9qZ1gn3xt++Dx6Y/f/mCv8KVnnvn+j378pG0KebGdjo8GLzUhxUxQcEBDre7bSC3asBaHemGknVtxQg40K9b13lQSmaMUxde19DOC9KJLOih3z8QMO7p9y91PznY3hv2LMa4/+3I7efTw/qNbN2/cGOpvfu7VX/7ip7v1Hr3ACkivhlIPktePT77w+mtPzzYJPx3no6ODBx88Xq/99Hy7HVe168ftphRaWzy3hZJ7ZsJNZpAhoEsOSTNDyizILN67WxunjG22qe8PaldJmllZzFMDpJymcTdtbt6+HXPMWcaxXeza1ZvPfPtHP7hx/eadPf2dL37iU5/9aB36hXQQMnOa06xf7R8cX30R8eq799549wOdb4y0Uh49Pd3cOpznSUKLttf3LVoIfolZgileuhOa20xw6V1mbK1Bkal5HgUCnilzs1IgSAmgLHsISz7WUlfDuu+H7/7wexHzz9/5+Ude+1zbbF96+SNHLz37lS99/PnbV3fTmWla1AzQQFPSSJVcHe7vzp9+6uMfffvdB5gCEUPfn5xsHp1s5imyNYczkVILOZVqZjbnHC29LCMssexBQLV4ANMUQGdel3UCZCe6l2oGd5qjLEg8Q6XUrpZSajV768c/uXvv0YufugJav15/6vOf/Jtf/MTm/jvnT+/V8gsMTNCq0yNhxpTWe/vntb925egjH3rxwZOzgpSilOHhk83FxWiKVdct7GuRRopbMd9AqfQFGKWWBxBw6e7QIEix2c2r1SEI5SyFFzenL6rqoqN03WqapqMrh0Tev3t3DtWW8fTxKy/d/Fu/+fmzu3d/8I0/f/LgLaLdunPz1p07/cExLylJao4Yp5zn9PL09PT2zavXjg/uP3mCbOac57zYtXVBpqxjKoGgmUZpMbui1VqcdFBQgClEKhZTAdptxlqquTUR5gkF0kqheYmIZQAuls66X2232ydPH9969qVbz9y6Uudfef2VubWz8/Nbd24XnT998uCtn//0/PHDlz768dXVW/KujdsH77x196237927tzrYa+Pu4mJz7fjK0fDgwclmUmuhi+14fLx2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"

MAYMAY_PHOTO_B64 = (
    "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRof"
    "Hh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwh"
    "MjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAAR"
    "CAEsASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgED"
    "AwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRol"
    "JicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWW"
    "l5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3"
    "+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3"
    "AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5"
    "OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanq"
    "KmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEA"
    "PwD2QSEU8T4600pTShqSSws6nqamBB6Gs4judeBzSAvYoAqATMOqmnCceh/KgCbbSFaYJ19ad5yHuKAA"
    "rTStP8xT3FIWFICMimlakJFNyKYDMU0ipOKQ0DIitNK1KaQgUAQlaYVqY4phoERFaaVqYimkUAQlaYy1"
    "YK0wrQBXK0wrxVgrTStIRWIphFWCtMZaAKxFMIqwyimFRQBXK0wrVghoyimFRQBXK0wrVkhoCimGRQBX"
    "K0wrVkhoCimGRQBXK0wrVghoCimGRQBXK0wrVkhoCimGRQBXK0wrVkhoCimGRQBVK0wrVghoBimGRQBXK"
    "0wrVghoCimGRQBXK0wrVkhoCimGRQBXK0wrVkhoCimGRQBXK0wrVkhoCimGRQBXK0wrVkhoCimGRQBXK0"
    "wrVkhoCimGRQBXK0wrVkhoCimFRQBWK0xhUzVGwosBFikNPIphGKVgGk03NONMPWiwAzcVGcZpxNRk0ID"
    "0NJY5CwR0bYdrbSDtPofegug64rzhdF1zUPEHiOLSNdk08R33mNFg7XZ1HJI5GMD2q5BZeKtKvLdL3WI"
    "b8S28qtiLaAdcFWPc9cVQHaPNGeAvJGah3FWHTn3qrI4SbHmLgKe9Iztui+ZeT60DLZuSDU8Um9a5+/v"
    "buzs5JbbT5b6RWXEMThWIJwcE8cdaydN8cXM8HnL4X1Z03MpaFVcZBwR1HcUkB3eaSKWKeMSRukiHoyk"
    "EH8a5MePII2H2jRNchwed1kT/I1ieEvGuk6Vohs717mMx3MxTNs5AQuSAcDg89KYHpJVfQU0qvuPxrmF"
    "+IXhduuqxJ/wBdEZf5ip08aeG5jhNbsT9ZgP50Bc3SB2Y/nTTkdJDVCPXdJmH7vU7N8+k6f41ILu3l/"
    "wBXPG3+64NIZazJ/fH4ijdIO6mue8GzvP4S06SWR5JDGdzMck4Zh1rez7mgB++T+6PzpDI3dDTc/wAC"
    "jzTc/wC0aC+e9FwEM2P4TTPPX3/KnZ96jYn2ouBIJAaXdUOTjoPzpQT6UXESFqaWpM57GkwPQ0AITTSa"
    "cQPemlc0AMJqNjUjAUwpQBETTDUpSmlKBEJpjVMUphSgCAioyKsFfamFDigCuVppWpihphU0AQkGoyKl"
    "YGomB70rgRmoyeae1RluaAOi0JgfGPikKwI82A8djswQfxrYu41b5yPmUEA+metc/wCGwF8d+MB/02gP"
    "5pXQ3hwhq2CMqVAXP0pgQfJgDipHb5qQdqzKJYExnHYf1rK8EnGiMPS6uB/5Faty3GZCPUVh+DSDpMwA"
    "xtvrlcZz/wAtDTQM6kSEdz+dc54QkY/26jqAV1ackD3xW8TXP+Gyi6x4mjRgQNQD4HYmNc/qDVCOieKC"
    "QYeCJv8AeQGqM+kaVN/rdMs3+tun+FXjaYx5oAxpfCfhuYHfodgfpCB/KqcngPws7DGjwpz/AMs2Zf5G"
    "ujpiUD3qbimBwPhrwdo19oNtcvbXsc7FwyR3TqvDsOADgcitf/hCLZf9RrWuQ+m29J/mK0/B6lPDsStwV"
    "mnGP+2rV0HQUgOZ/4RPUIx+48Xayn++Uf+YrM12y8S6NpM13B4quLhl2qsb2keSWIXqOnXNd12qGe3iu"
    "IjHMoZD1BoGcjPp/juC2Ag13T7iQAfftthP/AALkfpWtoK+IvsrDXpLFps/IbXPT/ayMflW4QMYoA4oA"
    "aM4wacGFBAoK+lIBwIPFPzUajFP6VSEGfelzTaKAFP0FIaKQ0xDSB6U0gegp9NI5pAMKr/dFMKrjlRUh"
    "pjdKAINq/wB0U0onp+tONNoAQxJ6H86TyUPrVDWotRuNOdNMvlsrjtKYg+B34P8AOuN0C38eX9hFdnxF"
    "bhHZyEubQO2ASBkjHBxmjQDvmihzjPNQPDAXK7iCPasbQk8QDVLn+2Ly0lhRdqeRAY/mz15J7VNr019b"
    "kyaXHbz3HGEnYqhHfkc0AXvskbHG/wDSkNjGD98flXIzeIvFdonmTaFpzJuCZjvSOTwOoqzaa/4gniZ7"
    "jQ1ibcQFSXeMfWgDmtO8V69pmqT6hFrenzzXRX7T58f+t28DsMceldonxLt7m3AubNVm7+Rcqyn6Zwa8r"
    "Jcj/Cky45xms/aM6vYxPSm+IEfmDbpcjJ6i5jz+Batl4w0m6A8yZrZu6zrj9RkV48HfPIH5UvmuCOBSu"
    "w9ij3P/AIS3QbMiSTUY2HpEC5/ICsbwhrmail3bXaxxyyXtxJGkqlCysxKnIGOnrXBeckbsOKDKSecU1I"
    "j2KPefD/AIz8PWHh22iuNQhgmTfkSqyscu3cD3rT/wCE+8Mn/mN2f/fw/wCFeACVj3pPNPvVc5HsUex+"
    "MPEnh3VvDVzb22qW0s7FNiI5LHDqemD2FcFY8WMH+4KKKG7jirI//9k="
)

# ── Constantes ──────────────────────────────────────────────────────────────
COLS, ROWS = 10, 20
BLOCK = 30
W_GAME = COLS * BLOCK          # 300
W_SIDE = 180
W_TOTAL = W_SIDE + W_GAME + W_SIDE
H_TOTAL = ROWS * BLOCK         # 600

FPS = 60

# Couleurs néon
BG        = (10, 10, 15)
PANEL_BG  = (15, 15, 26)
DIM       = (74, 74, 106)
ACCENT    = (0, 245, 255)
ACCENT2   = (255, 0, 110)
ACCENT3   = (255, 190, 11)
WHITE     = (224, 224, 255)

COLORS = {
    "I": ((0, 245, 255),   (0, 184, 196)),
    "O": ((255, 190, 11),  (204, 152, 0)),
    "T": ((184, 0, 255),   (136, 0, 204)),
    "S": ((0, 255, 136),   (0, 204, 102)),
    "Z": ((255, 0, 110),   (204, 0, 85)),
    "J": ((0, 102, 255),   (0, 68, 204)),
    "L": ((255, 102, 0),   (204, 68, 0)),
}

SHAPES = {
    "I": [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]],
    "O": [[1,1],[1,1]],
    "T": [[0,1,0],[1,1,1],[0,0,0]],
    "S": [[0,1,1],[1,1,0],[0,0,0]],
    "Z": [[1,1,0],[0,1,1],[0,0,0]],
    "J": [[1,0,0],[1,1,1],[0,0,0]],
    "L": [[0,0,1],[1,1,1],[0,0,0]],
}

SCORES   = [0, 100, 300, 500, 800]
SPEEDS   = [800, 700, 600, 500, 400, 300, 250, 200, 150, 100]  # ms


# ── Helpers ──────────────────────────────────────────────────────────────────
def load_photo():
    """Charge la photo Maymay depuis le base64 embarqué."""
    try:
        data = base64.b64decode(MAYMAY_PHOTO_B64)
        buf  = io.BytesIO(data)
        surf = pygame.image.load(buf, "maymay.jpg")
        surf = pygame.transform.scale(surf, (110, 110))
        return surf
    except Exception:
        return None


def draw_block(surface, x, y, piece_type, size=BLOCK, ghost=False, ox=0, oy=0):
    """Dessine un bloc avec effet néon."""
    c1, c2 = COLORS[piece_type]
    bx = ox + x * size
    by = oy + y * size
    rect = pygame.Rect(bx, by, size, size)

    if ghost:
        s = pygame.Surface((size, size), pygame.SRCALPHA)
        s.fill((*c1, 35))
        surface.blit(s, (bx, by))
        pygame.draw.rect(surface, (*c1, 80), rect, 1)
        return

    # Dégradé simulé : fond foncé puis clair
    pygame.draw.rect(surface, c2, rect)
    pygame.draw.rect(surface, c1, pygame.Rect(bx, by, size - 4, size - 4))

    # Reflet haut-gauche
    hl = pygame.Surface((size - 4, 4), pygame.SRCALPHA)
    hl.fill((255, 255, 255, 40))
    surface.blit(hl, (bx + 2, by + 2))

    # Bordure sombre
    pygame.draw.rect(surface, (0, 0, 0, 60), pygame.Rect(bx, by, size, size), 1)


def rotate_shape(shape):
    N, M = len(shape), len(shape[0])
    result = [[0]*N for _ in range(M)]
    for r in range(N):
        for c in range(M):
            result[c][N - 1 - r] = shape[r][c]
    return result


def render_text(font, text, color):
    return font.render(text, True, color)


# ── Classes ──────────────────────────────────────────────────────────────────
class Piece:
    def __init__(self, kind):
        self.kind  = kind
        self.shape = [row[:] for row in SHAPES[kind]]
        self.x     = COLS // 2 - len(self.shape[0]) // 2
        self.y     = 0

    def rotate(self):
        self.shape = rotate_shape(self.shape)

    def clone(self):
        p = Piece(self.kind)
        p.shape = [row[:] for row in self.shape]
        p.x, p.y = self.x, self.y
        return p


class TetrisGame:
    def __init__(self):
        self.board   = [[None]*COLS for _ in range(ROWS)]
        self.score   = 0
        self.lines   = 0
        self.level   = 1
        self.combo   = 1
        self.hi      = 0
        self.current = self._new_piece()
        self.next    = self._new_piece()
        self.over    = False
        self.paused  = False
        self._drop_acc = 0   # accumulateur ms

    def _new_piece(self):
        return Piece(random.choice(list(SHAPES.keys())))

    def _collides(self, piece, dx=0, dy=0, shape=None):
        sh = shape or piece.shape
        for r, row in enumerate(sh):
            for c, v in enumerate(row):
                if not v:
                    continue
                nx, ny = piece.x + c + dx, piece.y + r + dy
                if nx < 0 or nx >= COLS or ny >= ROWS:
                    return True
                if ny >= 0 and self.board[ny][nx]:
                    return True
        return False

    def _lock(self):
        for r, row in enumerate(self.current.shape):
            for c, v in enumerate(row):
                if v and self.current.y + r >= 0:
                    self.board[self.current.y + r][self.current.x + c] = self.current.kind
        self._clear_lines()
        self.current = self.next
        self.next    = self._new_piece()
        if self._collides(self.current):
            self.over = True

    def _clear_lines(self):
        cleared = 0
        r = ROWS - 1
        while r >= 0:
            if all(self.board[r]):
                del self.board[r]
                self.board.insert(0, [None]*COLS)
                cleared += 1
            else:
                r -= 1
        if cleared:
            self.combo  = min(self.combo + 1, 8)
            pts         = SCORES[cleared] * self.level * self.combo
            self.score += pts
            self.lines += cleared
            self.level  = min(10, self.lines // 10 + 1)
            self.hi     = max(self.hi, self.score)
        else:
            self.combo = 1

    def move(self, dx):
        if not self._collides(self.current, dx=dx):
            self.current.x += dx

    def rotate(self):
        rotated = rotate_shape(self.current.shape)
        kick = 0
        if self._collides(self.current, shape=rotated):
            kick = -1 if self.current.x + len(rotated[0]) > COLS else 1
        if not self._collides(self.current, dx=kick, shape=rotated):
            self.current.shape = rotated
            self.current.x += kick

    def soft_drop(self):
        if not self._collides(self.current, dy=1):
            self.current.y += 1
            self._drop_acc = 0
        else:
            self._lock()

    def hard_drop(self):
        while not self._collides(self.current, dy=1):
            self.current.y += 1
        self._lock()
        self._drop_acc = 0

    def ghost(self):
        g = self.current.clone()
        while not self._collides(g, dy=1):
            g.y += 1
        return g

    def update(self, dt_ms):
        """dt_ms : millisecondes écoulées depuis le dernier update."""
        if self.over or self.paused:
            return
        speed = SPEEDS[min(self.level - 1, len(SPEEDS) - 1)]
        self._drop_acc += dt_ms
        if self._drop_acc >= speed:
            self._drop_acc = 0
            if not self._collides(self.current, dy=1):
                self.current.y += 1
            else:
                self._lock()


# ── Rendu ────────────────────────────────────────────────────────────────────
class Renderer:
    def __init__(self, screen, photo):
        self.screen = screen
        self.photo  = photo
        self._init_fonts()
        self._glow_cache = {}

    def _init_fonts(self):
        pygame.font.init()
        # Police pixel si disponible, sinon monospace
        self.font_big   = pygame.font.SysFont("Courier New", 22, bold=True)
        self.font_med   = pygame.font.SysFont("Courier New", 16, bold=True)
        self.font_small = pygame.font.SysFont("Courier New", 11, bold=True)
        self.font_tiny  = pygame.font.SysFont("Courier New", 10)

    def _glow_surf(self, text, font, color, radius=3):
        key = (text, id(font), color, radius)
        if key in self._glow_cache:
            return self._glow_cache[key]
        base = font.render(text, True, color)
        w, h = base.get_size()
        glow = pygame.Surface((w + radius*4, h + radius*4), pygame.SRCALPHA)
        dim_color = (*color, 60)
        for ox in range(-radius, radius+1, 2):
            for oy in range(-radius, radius+1, 2):
                s = font.render(text, True, dim_color[:3])
                s.set_alpha(50)
                glow.blit(s, (radius*2 + ox, radius*2 + oy))
        glow.blit(base, (radius*2, radius*2))
        self._glow_cache[key] = (glow, radius*2, radius*2)
        return glow, radius*2, radius*2

    def draw_text_glow(self, text, font, color, cx, cy):
        surf, ox, oy = self._glow_surf(text, font, color)
        r = surf.get_rect(center=(cx + ox//2, cy + oy//2))
        self.screen.blit(surf, (r.x - ox, r.y - oy))

    def draw_panel_box(self, x, y, w, h, label, value, v_color=WHITE):
        pygame.draw.rect(self.screen, PANEL_BG, (x, y, w, h))
        pygame.draw.rect(self.screen, DIM, (x, y, w, h), 1)
        lbl = self.font_tiny.render(label.upper(), True, ACCENT)
        self.screen.blit(lbl, (x + 10, y + 8))
        val = self.font_med.render(str(value), True, v_color)
        self.screen.blit(val, (x + 10, y + 24))

    def draw_board(self, game, ox, oy):
        # Fond
        pygame.draw.rect(self.screen, (5, 5, 13), (ox, oy, W_GAME, H_TOTAL))
        # Grille
        for c in range(COLS + 1):
            pygame.draw.line(self.screen, (10, 10, 26),
                             (ox + c*BLOCK, oy), (ox + c*BLOCK, oy + H_TOTAL))
        for r in range(ROWS + 1):
            pygame.draw.line(self.screen, (10, 10, 26),
                             (ox, oy + r*BLOCK), (ox + W_GAME, oy + r*BLOCK))

        # Blocs posés
        for r, row in enumerate(game.board):
            for c, kind in enumerate(row):
                if kind:
                    draw_block(self.screen, c, r, kind, ox=ox, oy=oy)

        # Ghost
        g = game.ghost()
        for r, row in enumerate(g.shape):
            for c, v in enumerate(row):
                if v and g.y + r >= 0:
                    draw_block(self.screen, g.x + c, g.y + r, game.current.kind,
                               ghost=True, ox=ox, oy=oy)

        # Pièce courante
        for r, row in enumerate(game.current.shape):
            for c, v in enumerate(row):
                if v and game.current.y + r >= 0:
                    draw_block(self.screen, game.current.x + c,
                               game.current.y + r, game.current.kind, ox=ox, oy=oy)

        # Bordure lumineuse
        for i, col in enumerate([ACCENT, ACCENT2, ACCENT3, ACCENT]):
            alpha = 180 - i * 40
            s = pygame.Surface((W_GAME + 4, H_TOTAL + 4), pygame.SRCALPHA)
            pygame.draw.rect(s, (*col, alpha), s.get_rect(), 2 - (i // 2))
            self.screen.blit(s, (ox - 2 + i, oy - 2 + i))

    def draw_next(self, piece, x, y, w, h):
        pygame.draw.rect(self.screen, PANEL_BG, (x, y, w, h))
        pygame.draw.rect(self.screen, DIM, (x, y, w, h), 1)
        lbl = self.font_tiny.render("SUIVANT", True, ACCENT)
        self.screen.blit(lbl, (x + 10, y + 8))
        size = 22
        sh   = piece.shape
        off_x = (w - len(sh[0]) * size) // 2
        off_y = y + 28
        for r, row in enumerate(sh):
            for c, v in enumerate(row):
                if v:
                    draw_block(self.screen, c, r, piece.kind,
                               size=size, ox=x + off_x, oy=off_y)

    def draw_photo_block(self, x, y):
        """Affiche la photo de Maymay dans un cadre style blocs Tetris."""
        if not self.photo:
            return
        pw, ph = 110, 110
        # Fond + bordure dégradée
        border_colors = [ACCENT, ACCENT2, ACCENT3, (0, 255, 136)]
        pygame.draw.rect(self.screen, PANEL_BG, (x - 4, y - 4, pw + 8, ph + 8))
        pygame.draw.rect(self.screen, ACCENT, (x - 2, y - 2, pw + 4, ph + 4), 2)
        self.screen.blit(self.photo, (x, y))
        # Blocs déco aux coins
        bs = 12
        corners = [(x - bs, y - bs), (x + pw, y - bs),
                   (x - bs, y + ph), (x + pw, y + ph)]
        kinds = ["I", "Z", "O", "T"]
        for (cx, cy), k in zip(corners, kinds):
            c1, _ = COLORS[k]
            pygame.draw.rect(self.screen, c1, (cx, cy, bs, bs))
            glow = pygame.Surface((bs, bs), pygame.SRCALPHA)
            glow.fill((*c1, 80))
            self.screen.blit(glow, (cx, cy))

    def draw_button(self, text, x, y, w, h, hover=False):
        color = ACCENT if not hover else WHITE
        pygame.draw.rect(self.screen, PANEL_BG, (x, y, w, h))
        pygame.draw.rect(self.screen, color, (x, y, w, h), 1)
        t = self.font_small.render(text, True, color)
        tr = t.get_rect(center=(x + w // 2, y + h // 2))
        self.screen.blit(t, tr)
        return pygame.Rect(x, y, w, h)

    def draw_overlay(self, text, sub, btn_text, cx, cy):
        """Écran d'accueil / game over."""
        s = pygame.Surface((W_GAME, H_TOTAL), pygame.SRCALPHA)
        s.fill((5, 5, 13, 220))
        bx = W_SIDE
        self.screen.blit(s, (bx, 0))

        # Titre
        self.draw_text_glow(text, self.font_big, ACCENT, cx, cy - 80)

        # Photo
        if self.photo:
            px = cx - 55
            py = cy - 60
            self.draw_photo_block(px, py)

        # Sous-titre
        sub_surf = self.font_tiny.render(sub, True, DIM)
        self.screen.blit(sub_surf, sub_surf.get_rect(center=(cx, cy + 80)))

        # Bouton
        bw, bh = 160, 36
        btn_rect = pygame.Rect(cx - bw//2, cy + 100, bw, bh)
        return btn_rect

    def draw_hud(self, game):
        """Panneau gauche + droit."""
        self.screen.fill(BG)

        lx = 10   # panneau gauche X
        rx = W_SIDE + W_GAME + 10  # panneau droit X
        pw = W_SIDE - 20

        # ── Titre gauche ──
        self.draw_text_glow("MAY", self.font_big, ACCENT, lx + pw//2, 40)
        self.draw_text_glow("MAY", self.font_big, ACCENT, lx + pw//2, 65)
        t = self.font_tiny.render("CLASSIC", True, DIM)
        self.screen.blit(t, t.get_rect(center=(lx + pw//2, 88)))

        # ── Stats ──
        self.draw_panel_box(lx, 110, pw, 52, "Score", f"{game.score:,}")
        self.draw_panel_box(lx, 172, pw, 52, "Lignes", game.lines)
        self.draw_panel_box(lx, 234, pw, 52, "Niveau", game.level)

        # ── Contrôles ──
        controls = [
            ("←→", "Déplacer"),
            ("↑",  "Pivoter"),
            ("↓",  "Descendre"),
            ("SPC","Drop"),
            ("P",  "Pause"),
            ("R",  "Reset"),
        ]
        cy = 310
        for key, action in controls:
            k = self.font_tiny.render(key, True, ACCENT3)
            a = self.font_tiny.render(action, True, DIM)
            self.screen.blit(k, (lx + 10, cy))
            self.screen.blit(a, (lx + 42, cy))
            cy += 18

        # ── Panneau droit ──
        # Next piece
        self.draw_next(game.next, rx, 10, pw, 90)

        # Hi-score
        self.draw_panel_box(rx, 110, pw, 52, "Record", f"{game.hi:,}")

        # Combo
        self.draw_panel_box(rx, 172, pw, 52, "Combo",
                            f"×{game.combo}", v_color=ACCENT2)

        # Photo Maymay (droite)
        if self.photo:
            px = rx + (pw - 110) // 2
            self.draw_photo_block(px, 240)

        # Pause indicator
        if game.paused:
            pt = self.font_med.render("PAUSE", True, ACCENT3)
            self.screen.blit(pt, pt.get_rect(center=(rx + pw//2, 380)))


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    pygame.init()
    pygame.display.set_caption("MAYMAY")
    screen = pygame.display.set_mode((W_TOTAL, H_TOTAL), pygame.SCALED | pygame.RESIZABLE)
    # Touche F11 = plein écran
    fullscreen = False

    # Icône de fenêtre = tête de Maymay
    try:
        import base64, io
        icon_data = base64.b64decode(MAYMAY_ICON_B64)
        icon_surf = pygame.image.load(io.BytesIO(icon_data), "icon.png")
        icon_surf = pygame.transform.scale(icon_surf, (32, 32))
        pygame.display.set_icon(icon_surf)
    except Exception:
        pass
    clock  = pygame.time.Clock()

    photo    = load_photo()
    renderer = Renderer(screen, photo)
    game     = TetrisGame()

    # États : "menu" | "playing" | "gameover"
    state    = "menu"
    btn_rect = None

    BOARD_OX = W_SIDE
    BOARD_OY = 0
    CENTER_X = W_SIDE + W_GAME // 2
    CENTER_Y = H_TOTAL // 2

    # Répétition touches
    pygame.key.set_repeat(180, 60)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((W_TOTAL, H_TOTAL), pygame.FULLSCREEN | pygame.SCALED)
                    else:
                        screen = pygame.display.set_mode((W_TOTAL, H_TOTAL), pygame.SCALED | pygame.RESIZABLE)
                    renderer.screen = screen
                if state == "playing":
                    if event.key == pygame.K_LEFT:
                        game.move(-1)
                    elif event.key == pygame.K_RIGHT:
                        game.move(1)
                    elif event.key == pygame.K_DOWN:
                        game.soft_drop()
                    elif event.key == pygame.K_UP:
                        game.rotate()
                    elif event.key == pygame.K_SPACE:
                        game.hard_drop()
                    elif event.key == pygame.K_p:
                        game.paused = not game.paused
                    elif event.key == pygame.K_r:
                        game = TetrisGame()
                        state = "menu"
                elif state in ("menu", "gameover"):
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        game  = TetrisGame()
                        state = "playing"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_rect and btn_rect.collidepoint(event.pos):
                    game  = TetrisGame()
                    state = "playing"

        # ── Update ──
        if state == "playing":
            game.update(dt)
            if game.over:
                state = "gameover"

        # ── Draw ──
        renderer.draw_hud(game)
        renderer.draw_board(game, BOARD_OX, BOARD_OY)

        if state == "menu":
            btn_rect = renderer.draw_overlay(
                "MAYMAY", "CLASSIC ARCADE  ── EDITION ──", "▶ JOUER",
                CENTER_X, CENTER_Y)
            mx, my = pygame.mouse.get_pos()
            hover = btn_rect.collidepoint(mx, my)
            renderer.draw_button("▶  JOUER", btn_rect.x, btn_rect.y,
                                 btn_rect.w, btn_rect.h, hover)

        elif state == "gameover":
            sub = f"Score: {game.score:,}  |  Lignes: {game.lines}  |  Niv: {game.level}"
            btn_rect = renderer.draw_overlay(
                "GAME OVER", sub, "▶ REJOUER", CENTER_X, CENTER_Y)
            mx, my = pygame.mouse.get_pos()
            hover = btn_rect.collidepoint(mx, my)
            renderer.draw_button("▶  REJOUER", btn_rect.x, btn_rect.y,
                                 btn_rect.w, btn_rect.h, hover)

        pygame.display.flip()
        dt = clock.tick(FPS)


if __name__ == "__main__":
    main()
