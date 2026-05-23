import tkinter as tk
from tkinter import messagebox


class MainWindow:
    """Premium dark-themed Gold Price Prediction window."""

    # ── Colour palette ──────────────────────────────────────────────
    BG_DARK      = "#0d0d1a"
    BG_CARD      = "#151528"
    BG_INPUT     = "#1c1c35"
    GOLD         = "#f0c040"
    GOLD_LIGHT   = "#ffd966"
    GOLD_DIM     = "#b8860b"
    TEXT_PRIMARY  = "#eaeaea"
    TEXT_SECONDARY = "#9898b0"
    TEXT_MUTED   = "#5c5c72"
    GREEN        = "#4ecca3"
    RED          = "#e94560"
    BORDER       = "#2a2a48"

    def __init__(self, root, on_predict):
        self.root = root
        self.on_predict = on_predict
        self._setup_window()
        self._build_ui()
        self._bind_events()

    # ── Window setup ────────────────────────────────────────────────
    def _setup_window(self):
        self.root.title("Gold Price Prediction")
        self.root.configure(bg=self.BG_DARK)
        self.root.resizable(False, False)

        w, h = 560, 740
        self.root.geometry(f"{w}x{h}")
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth()  - w) // 2
        y = (self.root.winfo_screenheight() - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    # ── Event bindings ──────────────────────────────────────────────
    def _bind_events(self):
        self.root.bind("<Return>", lambda _: self._predict_clicked())

    # ── UI construction ─────────────────────────────────────────────
    def _build_ui(self):
        outer = tk.Frame(self.root, bg=self.BG_DARK)
        outer.pack(fill="both", expand=True, padx=28, pady=24)

        self._build_header(outer)
        self._build_separator(outer)
        self._build_input_card(outer)
        self._build_results_card(outer)
        self._build_footer(outer)

    # ── Header ──────────────────────────────────────────────────────
    def _build_header(self, parent):
        hdr = tk.Frame(parent, bg=self.BG_DARK)
        hdr.pack(fill="x", pady=(0, 6))

        # Gold diamond icon
        tk.Label(
            hdr, text="\u2B25", font=("Segoe UI", 38),
            fg=self.GOLD, bg=self.BG_DARK,
        ).pack()

        tk.Label(
            hdr, text="GOLD PRICE PREDICTOR",
            font=("Segoe UI", 20, "bold"),
            fg=self.GOLD_LIGHT, bg=self.BG_DARK,
        ).pack(pady=(2, 0))

        tk.Label(
            hdr, text="ARIMA-Powered Monthly Forecasting Engine",
            font=("Segoe UI", 9),
            fg=self.TEXT_SECONDARY, bg=self.BG_DARK,
        ).pack(pady=(2, 0))

    # ── Thin gold separator ─────────────────────────────────────────
    def _build_separator(self, parent):
        sep = tk.Canvas(parent, height=2, bg=self.BG_DARK,
                        highlightthickness=0)
        sep.pack(fill="x", pady=(10, 14))
        sep.bind("<Configure>",
                 lambda e: sep.create_line(
                     0, 1, e.width, 1, fill=self.GOLD_DIM, width=1))

    # ── Input card ──────────────────────────────────────────────────
    def _build_input_card(self, parent):
        card = tk.Frame(parent, bg=self.BG_CARD,
                        highlightbackground=self.BORDER,
                        highlightthickness=1)
        card.pack(fill="x", pady=(0, 14))

        inner = tk.Frame(card, bg=self.BG_CARD)
        inner.pack(fill="x", padx=22, pady=18)

        tk.Label(
            inner, text="TARGET YEAR",
            font=("Segoe UI", 9, "bold"),
            fg=self.TEXT_SECONDARY, bg=self.BG_CARD,
        ).pack(anchor="w")

        # Row: entry + button
        row = tk.Frame(inner, bg=self.BG_CARD)
        row.pack(fill="x", pady=(8, 0))

        self.year_entry = tk.Entry(
            row,
            font=("Segoe UI", 18),
            bg=self.BG_INPUT,
            fg=self.TEXT_PRIMARY,
            insertbackground=self.GOLD,
            relief="flat",
            highlightbackground=self.BORDER,
            highlightthickness=1,
            highlightcolor=self.GOLD,
            justify="center",
        )
        self.year_entry.pack(side="left", fill="x", expand=True, ipady=6)
        self.year_entry.insert(0, "2026")
        self.year_entry.focus_set()

        self.predict_btn = tk.Button(
            row,
            text="  PREDICT  \u25B8  ",
            font=("Segoe UI", 12, "bold"),
            bg=self.GOLD,
            fg="#1a1a2e",
            activebackground=self.GOLD_LIGHT,
            activeforeground="#0f0f1a",
            relief="flat",
            cursor="hand2",
            bd=0,
            padx=18, pady=8,
            command=self._predict_clicked,
        )
        self.predict_btn.pack(side="right", padx=(12, 0), ipady=2)

        # Hover glow on button
        self.predict_btn.bind("<Enter>",
            lambda _: self.predict_btn.config(bg=self.GOLD_LIGHT))
        self.predict_btn.bind("<Leave>",
            lambda _: self.predict_btn.config(bg=self.GOLD))

        tk.Label(
            inner, text="Enter a year from 2026 onwards  \u2022  Press Enter to predict",
            font=("Segoe UI", 8),
            fg=self.TEXT_MUTED, bg=self.BG_CARD,
        ).pack(anchor="w", pady=(6, 0))

    # ── Results card ────────────────────────────────────────────────
    def _build_results_card(self, parent):
        card = tk.Frame(parent, bg=self.BG_CARD,
                        highlightbackground=self.BORDER,
                        highlightthickness=1)
        card.pack(fill="both", expand=True)

        # Card header row
        top = tk.Frame(card, bg=self.BG_CARD)
        top.pack(fill="x", padx=22, pady=(14, 0))

        tk.Label(
            top, text="\u25C8  FORECAST RESULTS",
            font=("Segoe UI", 9, "bold"),
            fg=self.TEXT_SECONDARY, bg=self.BG_CARD,
        ).pack(side="left")

        self.status_label = tk.Label(
            top, text="\u25CF  READY",
            font=("Segoe UI", 8, "bold"),
            fg=self.GREEN, bg=self.BG_CARD,
        )
        self.status_label.pack(side="right")

        # Text area with scrollbar
        txt_border = tk.Frame(card, bg=self.BORDER)
        txt_border.pack(fill="both", expand=True, padx=22, pady=(10, 18))

        txt_inner = tk.Frame(txt_border, bg=self.BG_INPUT)
        txt_inner.pack(fill="both", expand=True, padx=1, pady=1)

        scrollbar = tk.Scrollbar(txt_inner, orient="vertical",
                                 troughcolor=self.BG_INPUT,
                                 bg=self.BORDER,
                                 activebackground=self.GOLD_DIM,
                                 highlightthickness=0, bd=0)
        scrollbar.pack(side="right", fill="y")

        self.result_text = tk.Text(
            txt_inner,
            font=("Consolas", 11),
            bg=self.BG_INPUT,
            fg=self.TEXT_PRIMARY,
            relief="flat",
            wrap="word",
            padx=16, pady=14,
            insertbackground=self.GOLD,
            selectbackground=self.GOLD_DIM,
            selectforeground=self.TEXT_PRIMARY,
            state="disabled",
            yscrollcommand=scrollbar.set,
            cursor="arrow",
        )
        self.result_text.pack(fill="both", expand=True)
        scrollbar.config(command=self.result_text.yview)

        # Text tags for coloured output
        self.result_text.tag_configure("gold",
            foreground=self.GOLD_LIGHT, font=("Consolas", 11, "bold"))
        self.result_text.tag_configure("avg",
            foreground=self.GOLD, font=("Consolas", 12, "bold"))
        self.result_text.tag_configure("muted",
            foreground=self.TEXT_MUTED, font=("Consolas", 10))
        self.result_text.tag_configure("divider",
            foreground=self.BORDER)

        # Welcome placeholder
        self._set_result_text(
            "     \u2B25  Enter a year and click PREDICT\n"
            "        to generate monthly gold price\n"
            "        forecasts in INR and USD.",
            tag="muted",
        )

    # ── Footer ──────────────────────────────────────────────────────
    def _build_footer(self, parent):
        tk.Label(
            parent,
            text="Powered by ARIMA  \u2022  Prices in INR & USD  \u2022  Monthly Granularity",
            font=("Segoe UI", 8),
            fg=self.TEXT_MUTED, bg=self.BG_DARK,
        ).pack(pady=(10, 0))

    # ── Helpers ─────────────────────────────────────────────────────
    def _set_result_text(self, text, tag=None):
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", "end")
        if tag:
            self.result_text.insert("end", text, tag)
        else:
            self.result_text.insert("end", text)
        self.result_text.config(state="disabled")

    def _predict_clicked(self):
        raw = self.year_entry.get().strip()

        # Validate input is a number
        if not raw.isdigit():
            messagebox.showerror("Invalid Input",
                                 "Please enter a valid year (e.g. 2026).")
            self.status_label.config(text="\u25CF  ERROR", fg=self.RED)
            return

        year = int(raw)

        # Show processing state
        self.status_label.config(text="\u25CF  PROCESSING\u2026", fg=self.GOLD)
        self.predict_btn.config(state="disabled", bg=self.GOLD_DIM)
        self.root.update()

        try:
            result = self.on_predict(year)

            self._set_result_text(result)
            self.status_label.config(text="\u25CF  COMPLETE", fg=self.GREEN)

        except Exception as e:
            messagebox.showerror("Prediction Error", str(e))
            self.status_label.config(text="\u25CF  ERROR", fg=self.RED)

        finally:
            self.predict_btn.config(state="normal", bg=self.GOLD)
