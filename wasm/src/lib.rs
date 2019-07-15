use difflib::differ::Differ;
use std::{
    ffi::{CStr, CString},
    mem,
    os::raw::{c_char, c_void},
};

#[no_mangle]
pub extern "C" fn allocate(size: usize) -> *mut c_void {
    let mut buffer = Vec::with_capacity(size);
    let pointer = buffer.as_mut_ptr();

    mem::forget(buffer);

    pointer as *mut c_void
}

#[no_mangle]
pub extern "C" fn deallocate(ptr: *mut u8, capacity: usize) -> i32 {
    unsafe {
        let _ = Vec::from_raw_parts(ptr, 0, capacity);
    }

    1
}

#[no_mangle]
pub extern "C" fn compare(first: *const c_char, second: *const c_char) -> *const c_char {
    assert!(!first.is_null());
    assert!(!second.is_null());

    let first_str = unsafe { CStr::from_ptr(first).to_str().unwrap() };
    let second_str = unsafe { CStr::from_ptr(second).to_str().unwrap() };

    let first_lines: Vec<&str> = first_str.split("\n").collect::<Vec<&str>>();
    let second_lines: Vec<&str> = second_str.split("\n").collect::<Vec<&str>>();

    // // Differ examples
    let differ = Differ::new();
    let diff = differ.compare(&first_lines, &second_lines);

    CString::new(diff.join("\n")).unwrap().into_raw()
}
