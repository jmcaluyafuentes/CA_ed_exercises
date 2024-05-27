


create table students (
    student_id serial primary key,
    f_name text not null,
    l_name text not null,
    dob date,
    email text not null
)