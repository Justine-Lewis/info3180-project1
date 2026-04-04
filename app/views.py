"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from .forms import PropertyForm
from .models import Property

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


#Create Properties Page - to add properties through property form
@app.route('/properties/create', methods=['POST', 'GET'])
def addproperty():
    form = PropertyForm()

    if form.validate_on_submit():
        title = form.title.data
        bedrooms = form.bedrooms.data
        bathrooms = form.bathrooms.data
        location = form.location.data
        price = form.price.data
        property_type = form.property_type.data
        description = form.description.data

        photo = form.photo.data
        filename = secure_filename(photo.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(upload_path)

        property_item = Property(
            title=title,
            description=description,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            location=location,
            price=price,
            property_type=property_type,
            photo=filename
        )

        db.session.add(property_item)
        db.session.commit()

        flash('Property added successfully.', 'success')
        return redirect(url_for('properties'))

    return render_template('addproperty.html', form=form)

@app.route('/properties', methods=['GET'])
def properties():
    property_list = Property.query.all()
    return render_template('properties.html', properties=property_list) 

@app.route('/properties/<propertyid>', methods=['GET'])
def property_view(propertyid):
    property_item = Property.query.get_or_404(propertyid)
    return render_template('property_view.html', property=property_item)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
