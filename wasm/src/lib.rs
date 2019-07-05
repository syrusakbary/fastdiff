use std::ffi::{CStr, CString};
use std::mem;
use std::os::raw::{c_char, c_void};
use difflib::differ::Differ;

#[no_mangle]
pub extern fn allocate(size: usize) -> *mut c_void {
    let mut buffer = Vec::with_capacity(size+1);
    let pointer = buffer.as_mut_ptr();
    mem::forget(buffer);

    pointer as *mut c_void
}

#[no_mangle]
pub extern fn deallocate(pointer: *mut c_void, capacity: usize) {
    unsafe {
        let _ = Vec::from_raw_parts(pointer, 0, capacity);
    }
}

#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

#[no_mangle]
fn compare(first: *const c_char, second: *const c_char) -> *const c_char {
    let first_str = unsafe { CStr::from_ptr(first).to_str().unwrap() };
    let second_str = unsafe { CStr::from_ptr(second).to_str().unwrap() };

    // let first_str = "a";
    // let second_str = "b";
    
    let first_lines: Vec<&str> = first_str.split("\n").collect::<Vec<&str>>();
    let second_lines: Vec<&str> = second_str.split("\n").collect::<Vec<&str>>();

    // // Differ examples
    let differ = Differ::new();
    let diff = differ.compare(&first_lines, &second_lines);
    // // for line in &diff {
    // //     println!("{:?}", line);
    // // }
    // CString::new(diff.join("\n")).unwrap().as_ptr() as _

    CString::new(diff.join("\n")).unwrap().into_raw()
    // first
}
