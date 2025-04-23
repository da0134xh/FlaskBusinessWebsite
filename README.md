# FlaskBusinessWebsite
Extra Credit - Creating a Flask Business Website with Bootstrap

Using the SQLite Command Line in Codespaces

You can interact with your database directly using the SQLite command-line tool in your Codespaces terminal:

# First, locate your database file ls -la instance/ 
# Open the database (adjust path if needed) sqlite3 instance/business_site.db 
# List all tables .tables # View all contacts SELECT * FROM contact; 
# View specific columns SELECT name, email, date_submitted FROM contact; 
# Filter entries SELECT * FROM contact WHERE name LIKE '%John%'; 
# Exit SQLite .

If you want to export your database data to review it more easily:

# Enter the SQLite CLI sqlite3 instance/business_site.db 
# Set output format to CSV .mode csv .header on 
# Export to a file .output contacts.csv SELECT * FROM contact; .output stdout 
# Exit SQLite .exit 
# View the exported file cat contacts.csv