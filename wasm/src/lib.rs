use std::ffi::{CStr, CString};
use std::mem;
use std::alloc::{alloc, dealloc, realloc, Layout};
use std::os::raw::{c_char, c_void};
use difflib::differ::Differ;

#[no_mangle]
pub unsafe extern fn allocate(size: usize) -> *mut u8 {
    let align = mem::align_of::<usize>();
    if let Ok(layout) = Layout::from_size_align(size, align) {
        unsafe {
            if layout.size() > 0 {
                let ptr = alloc(layout);
                if !ptr.is_null() {
                    return ptr
                }
            } else {
                return align as *mut u8
            }
        }
    }
    std::process::abort();
}

// #[no_mangle]
// pub extern "C" fn caco() -> i32 {
//     return 2
// }

#[no_mangle]
pub unsafe extern fn deallocate(ptr: *mut u8, capacity: usize) -> i32 {
    if capacity == 0 {
        return 0
    }
    let align = mem::align_of::<usize>();
    let layout = Layout::from_size_align_unchecked(capacity, align);
    dealloc(ptr, layout);
    1
}

// #[global_allocator]
// static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

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
