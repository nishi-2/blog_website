from flask import Blueprint, render_template

python_bp = Blueprint('python_bp', __name__, url_prefix='/ml')


@python_bp.route('/')
def ml_page():
    return render_template('landing_page_directing_to_templates/python_page.html')


#begineer page links
@python_bp.route('/python/begineer')
def python_begineer_page():
    return render_template('python_templates/python_blogs/python_blogs_begineer_page.html')


@python_bp.route('/python/begineer/introduction_to_python')
def python_begineer_intoduction_to_python_page():
    return render_template('python_templates/python_blogs/blogs/begineer/introduction_to_python.html')


@python_bp.route('/python/begineer/literals_variables_print')
def python_begineer_part_2_blog():
    return render_template('python_templates/python_blogs/blogs/begineer/part_2_python_blog.html')



#OOPS page links
@python_bp.route('/python/oops')
def python_oops_page():
    return render_template('python_templates/python_blogs/python_blogs_oops_page.html')


@python_bp.route('/python/oops/nodes_intro')
def python_oops_nodes_intro_page():
    return render_template('python_templates/python_blogs/blogs/oops/Part_1_Node.html')

@python_bp.route('/python/oops/singly_linked_list')
def python_oops_singly_linked_list_page():
    return render_template('python_templates/python_blogs/blogs/oops/Part_2_SinglyLinkedListFull.html')

@python_bp.route('/python/oops/doubly_linked_list')
def python_oops_doubly_linked_list_page():
    return render_template('python_templates/python_blogs/blogs/oops/Part_3_DoublyLinkedListFull.html')


# Project End points
