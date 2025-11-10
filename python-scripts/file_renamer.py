"""
entry_path.delete(0, tk.END)
entry_path.insert(0, folder)

def run_rename():
folder = entry_path.get()
prefix = entry_prefix.get() or "renamed_"
try:
rename_files(folder, prefix)
messagebox.showinfo("Success", "Files renamed successfully!")
except Exception as e:
messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("File Renamer GUI")

tk.Label(root, text="Folder Path:").pack()
entry_path = tk.Entry(root, width=40)
entry_path.pack()

tk.Button(root, text="Browse", command=select_folder).pack()

tk.Label(root, text="Prefix:").pack()
entry_prefix = tk.Entry(root, width=40)
entry_prefix.pack()

tk.Button(root, text="Rename Files", command=run_rename).pack(pady=10)
root.mainloop()


# ------------------------- CLI Interface ----------------------

if __name__ == "__main__":
parser = argparse.ArgumentParser(description="Enhanced file renamer with undo and GUI.")
subparsers = parser.add_subparsers(dest="command")

rename_parser = subparsers.add_parser("rename")
rename_parser.add_argument("--path", required=True, help="Path to directory of files")
rename_parser.add_argument("--prefix", default="renamed_", help="Prefix for new files")
rename_parser.add_argument("--start", type=int, default=1, help="Starting index number")

subparsers.add_parser("undo")
subparsers.add_parser("gui")

args = parser.parse_args()

if args.command == "rename":
rename_files(args.path, args.prefix, args.start)
elif args.command == "undo":
undo_last_rename()
elif args.command == "gui":
open_gui()
else:
parser.print_help()
