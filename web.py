import streamlit as st
from math_function import drawing_triangle, distance_between_two_pt, equation_of_st_line
import multiprocessing


st.title("Evan's MathSolverPro")

st.caption("This website can draw a right-angled triangle and calculate the equation of straight line by given two points")




with st.expander("Draw a right angle triangle"):        
    # drawing traingle
    st.header("draw triangle(angle 1 plus angle 2 needs to be equal to 90)")

    st.subheader("angle1")
    angle1 = st.number_input("pick angle1", 0, 90, value = 45)

    st.subheader("angle2")
    angle2 = st.number_input("pick angle2", 0, 90, value = 45)

    if angle1 + angle2 != 90:
        st.error("angle 1 plus angle 2 needs to be equal to 90")

    st.subheader("height")
    h = st.number_input("pick h", 0, 150, value = 50)
    
    if st.button("Draw") and angle1 + angle2 == 90:

        angle3 = 90

        t = multiprocessing.Process(target = drawing_triangle, args = (angle1, angle2, h))
        t.start()

with st.expander("two point formula"):
    # euqation of staright line
    st.header("Calculation equation of straight line with two point formula")

    st.subheader("x of point 1")
    x1 = st.number_input("pick a number for x1", -100, 100, value = 0)

    st.subheader("y of point 1")
    y1 = st.number_input("pick a number for y1", -100, 100, value = 0)

    st.subheader("x of point 2")
    x2 = st.number_input("pick a number for x2", -100, 100, value = 0)

    st.subheader("y of point 2")
    y2 = st.number_input("pick a number for y2", -100, 100, value = 0)



    if st.button("equation of straight line"):
        answer = equation_of_st_line(x1,y1,x2,y2)
        st.write(f"The equation of this line is {answer}")
        


    if st.button("distance between two points"):
        answer = distance_between_two_pt(x1,y1,x2,y2)
        st.write(f"The distance is {answer} units")








