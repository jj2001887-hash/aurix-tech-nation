import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-before-deploying")

COURSES = [
    {"id":"web-development","number":"01","title":"Web Development","price":"KSh 15,000","duration":"12 weeks · 3 months","schedule":"3 classes per week · 2 hours per class","description":"Build responsive websites with HTML, CSS, JavaScript, and practical projects.","topics":["HTML & CSS foundations","JavaScript fundamentals","Responsive design","Build and publish a project"]},
    {"id":"graphic-design","number":"02","title":"Graphic Design & Canva","price":"KSh 15,000","duration":"12 weeks · 3 months","schedule":"3 classes per week · 2 hours per class","description":"Create logos, posters, flyers, social graphics, business cards, and brand materials.","topics":["Design principles","Canva workflow","Posters and social graphics","Brand identity basics"]},
    {"id":"excel-data","number":"03","title":"Microsoft Excel & Data Skills","price":"KSh 15,000","duration":"12 weeks · 3 months","schedule":"3 classes per week · 2 hours per class","description":"Organize data, use formulas, create charts, and prepare clear reports.","topics":["Spreadsheets and formulas","Data cleaning and organization","Charts and reports","Introductory data analysis"]},
    {"id":"python","number":"04","title":"Python Programming","price":"Enquire for fees","duration":"To be confirmed","schedule":"Timetable to be confirmed","description":"Learn programming fundamentals, automation, and problem-solving through projects.","topics":["Python fundamentals","Conditions and loops","Functions and data structures","Practical mini-projects"]},
    {"id":"ai","number":"05","title":"Artificial Intelligence & Prompt Engineering","price":"Enquire for fees","duration":"To be confirmed","schedule":"Timetable to be confirmed","description":"Explore AI tools, prompt writing, productivity workflows, and responsible AI use.","topics":["Prompt design","AI-assisted productivity","Content workflows","Responsible AI"]},
    {"id":"cybersecurity","number":"06","title":"Cybersecurity & Digital Safety","price":"Enquire for fees","duration":"To be confirmed","schedule":"Timetable to be confirmed","description":"Build safer digital habits and understand common online threats.","topics":["Password security","Phishing awareness","Privacy basics","Device and account safety"]},
    {"id":"computer-packages","number":"07","title":"Computer Packages","price":"Enquire for fees","duration":"To be confirmed","schedule":"Timetable to be confirmed","description":"Develop confidence with computer basics, documents, spreadsheets, and presentations.","topics":["Computer fundamentals","Word processing","Spreadsheets","Presentations and files"]},
    {"id":"digital-marketing","number":"08","title":"Digital Marketing","price":"Enquire for fees","duration":"To be confirmed","schedule":"Timetable to be confirmed","description":"Plan digital content, strengthen online branding, and understand campaign basics.","topics":["Social media strategy","Content planning","Online branding","Campaign fundamentals"]},
]

BOTS = [
    {"name":"TALK-SPAR TECH","tag":"AURIX bot project","description":"A WhatsApp bot project with a Telegram entry point.","telegram":"https://t.me/tlk_tech_bot","pairing":None,"featured":False},
    {"name":"TALKLESS XMD","tag":"Main bot","description":"The main bot project, with separate pairing options for website and Telegram users.","telegram":"https://t.me/Talkless_xmd_bot","pairing":"https://talkless-ultra-pair.vercel.app","featured":True},
    {"name":"AURIX-TECH HUB","tag":"AURIX bot project","description":"Explore the AURIX-TECH HUB Telegram bot.","telegram":"https://t.me/Talkless_mini_bot","pairing":None,"featured":False},
]

SERVICES = [
    ("Web Design & Development","Business websites, portfolios, landing pages, online catalogues, and maintenance."),
    ("Logo & Brand Identity","Logo concepts, brand colours, typography, and visual identity."),
    ("Graphic Design & Advertising","Posters, flyers, banners, business cards, invitations, and promotional artwork."),
    ("WhatsApp Bot Development","Bot setup, pairing assistance, custom commands, and maintenance."),
    ("AI & Automation","Practical AI integrations and workflow automation."),
    ("Data & Productivity","Excel solutions, charts, reports, and spreadsheet organization."),
    ("Digital Marketing","Social media content, campaigns, and online branding."),
    ("Technical Support","Website troubleshooting, software setup, and project assistance."),
]

@app.context_processor
def inject_globals():
    return {
        "year": datetime.now().year,
        "tech_channels": [
            ("AURIX BOTS TECH", "https://whatsapp.com/channel/0029VbCW8tNHwXb9rMHi7h0T"),
            ("TECH NATION CHANNEL", "https://whatsapp.com/channel/0029VakmDdTCnA7zAD7VvH3c"),
        ],
        "contact_phone_1": "+254 113 532 390",
        "contact_phone_2": "+254 741 175 487",
        "bot_support": "+254 799 984 735",
        "contact_email": "TECHNATION078@GMAIL.COM",
        "telegram_support": "https://t.me/Clavins",
        "instagram": "https://www.instagram.com/clavohh?psln=Z2NvNjZndHRieHBo",
    }

@app.route("/")
def home():
    return render_template("index.html", courses=COURSES[:3], bots=BOTS, services=SERVICES[:4])

@app.route("/courses")
def courses():
    return render_template("courses.html", courses=COURSES)

@app.route("/courses/<course_id>")
def course_detail(course_id):
    course = next((c for c in COURSES if c["id"] == course_id), None)
    if course is None:
        return render_template("404.html"), 404
    return render_template("course_detail.html", course=course)

@app.route("/bots")
def bots():
    return render_template("bots.html", bots=BOTS)

@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        category = request.form.get("category", "General enquiry").strip()
        message = request.form.get("message", "").strip()
        if not name or not email or not message:
            flash("Please complete your name, email, and message.", "error")
            return render_template("contact.html")
        # Starter behavior: no email is sent and no message is stored.
        # Connect an email provider or database before using this form in production.
        app.logger.info("Contact enquiry received: category=%s name=%s email=%s", category, name, email)
        flash("Thanks! The demo form accepted your enquiry. To receive messages, connect an email or database service before launch.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=os.environ.get("FLASK_DEBUG") == "1")
