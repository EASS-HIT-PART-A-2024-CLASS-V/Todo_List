import streamlit as st
import httpx
from model import Todo

# Base URL for the API
backend_url = "http://backend:8000"

# Custom CSS for the new design
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
        color: #333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
    }
    .container {
        max-width: 800px;
        margin: 20px auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #007bff;
        text-align: center;
        margin-bottom: 20px;
    }
    h2 {
        color: #007bff;
        margin-bottom: 20px;
    }
    .menu {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .menu a {
        color: #007bff;
        text-decoration: none;
        margin: 0 10px;
        padding: 5px 10px;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .menu a:hover {
        background-color: #007bff;
        color: #fff;
    }
    .button-primary {
        background-color: #007bff;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .button-primary:hover {
        background-color: #0056b3;
    }
    .button-danger {
        background-color: #dc3545;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .button-danger:hover {
        background-color: #c82333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
def main():
    st.markdown("<h1>Task Manager</h1>", unsafe_allow_html=True)

    menu = ["Home", "View Tasks", "Add Task", "Update Task", "Delete Task"]
    choice = st.selectbox("Menu", menu, index=0)

    if choice == "Home":
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.markdown("<h2>Welcome to the Task Manager!</h2>", unsafe_allow_html=True)
        st.markdown("<p>This is a simple task manager application.</p>", unsafe_allow_html=True)
        st.markdown("<p>Please use the menu above to navigate.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    elif choice == "View Tasks":
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.markdown("<h2>View Tasks</h2>", unsafe_allow_html=True)
        response = httpx.get(f"{backend_url}/api/todo/all")
        tasks = response.json()
        if isinstance(tasks, list):
            for task in tasks:
                st.markdown(f"<p><strong>Title:</strong> {task['title']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p><strong>Description:</strong> {task['description']}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p>No tasks available.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    elif choice == "Add Task":
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.markdown("<h2>Add Task</h2>", unsafe_allow_html=True)
        title = st.text_input("Title")
        description = st.text_area("Description")
        if st.button("Add Task", key="add_task", help="button-primary"):
            task = Todo(title=title, description=description)
            response = httpx.post(f"{backend_url}/api/todo/add", json=task.dict())
            if response.status_code == 200:
                st.success("Task added successfully!")
            else:
                st.error("Failed to add task. Please try again later.")
        st.markdown("</div>", unsafe_allow_html=True)

    elif choice == "Update Task":
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.markdown("<h2>Update Task</h2>", unsafe_allow_html=True)
        title = st.text_input("Title")
        description = st.text_area("Description")
        if st.button("Update Task", key="update_task", help="button-primary"):
            response = httpx.put(f"{backend_url}/api/todo/update/{title}", json={"title": title, "description": description})
            if response.status_code == 200:
                st.success("Task updated successfully!")
            else:
                st.error("Failed to update task. Please make sure the title exists and try again.")
        st.markdown("</div>", unsafe_allow_html=True)

    elif choice == "Delete Task":
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.markdown("<h2>Delete Task</h2>", unsafe_allow_html=True)
        title = st.text_input("Title")
        if st.button("Delete Task", key="delete_task", help="button-danger"):
            response = httpx.delete(f"{backend_url}/api/todo/delete/{title}")
            if response.status_code == 200:
                st.success("Task deleted successfully!")
            else:
                st.error("Failed to delete task. Please make sure the title exists and try again.")
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
