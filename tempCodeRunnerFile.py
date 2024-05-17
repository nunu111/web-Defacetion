# Frame for Text Editor
        self.text_frame = tk.Frame(self.root, width=400, height=300)
        self.text_frame.pack(padx=10, pady=10, expand=True, fill='both')
        self.text_frame.pack_propagate(False)  # Prevent frame from resizing to fit content

        # Text Widget for displaying and editing the content
        self.text = tk.Text(self.text_frame, wrap='word')
        self.text.pack(expand=1, fill='both', side='left')