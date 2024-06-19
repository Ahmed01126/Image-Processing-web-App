var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

let image_1 = ""
let image_2 = ""
let Upload_First_Image = document.querySelector('#image_input1')
let Upload_Second_Image = document.querySelector('#image_input2')
let result1 = document.querySelector('#result1')
let result2 = document.querySelector('#result2')
let submit = document.getElementById("combine_btn")
let cb1 = document.getElementById("uniform-phase")
let cb2 = document.getElementById("uniform-Magnitude")
let opt = document.getElementById("image1_info")
let x11, x21, x12, x22, y11, y21, y12, y22

function cb_check(){
  cb_ph = document.querySelector('#uniform-phase').checked;
  cb_amp = document.querySelector('#uniform-Magnitude').checked;
}


function sData(){
  
  try {
    const ch = document.getElementById("image1_info");
    if (image_1 == "" || image_2 == "") {
      throw "error : not enough images "
    }
    cb_check()

    $.ajax({
      type: 'POST',
      url: '/saveImg',
      data: {
        original_1: image_1,
        original_2: image_2,
        ch: ch.value,
        x11: x11,
        x21: x21,
        y11: y11,
        y21: y21,
        x12: x12,
        x22: x22,
        y12: y12,
        y22: y22,
        cb_ph: cb_ph,
        checkbox_Magnitude: cb_amp
      },
      success: function (response) {
        var responce = JSON.parse(response)
        var big_cont = document.getElementById("images_container")
        const cont12 = document.getElementById("cont1")
        cont12.remove()
        var img_1 = document.createElement("div")
        img_1.className = "container"
        img_1.id = "cont1"
        img_1.innerHTML = responce[1]
        big_cont.appendChild(img_1)

      }
    })
  }  
  catch (error) {
  }  
}

Upload_First_Image.addEventListener('change', function() {
    const reader = new FileReader();
    reader.addEventListener ("load",()=>{
       let pass=reader.result
        let img = document.createElement('img');
        img.id = 'image';
        img.src = pass;
        result1.innerHTML = '';
        result1.appendChild(img)
        image_1 = pass
        cropper1 = new Cropper(img, {
          zoomOnWheel: false,
          movable: false,
          guides: false,
          crop: function (co) {
            x11 = co.detail.x
            y11 = co.detail.y
            y21 = co.detail.height + co.detail.y
            x21 = co.detail.width + co.detail.x
          },
          cropend: function(e){
            sData()
          }
        });
      
    });
    reader.readAsDataURL(this.files[0]);
  
});
Upload_Second_Image.addEventListener('change',function() {

    const reader = new FileReader();
    reader.addEventListener ("load",()=>{
        let pass=reader.result
        let img2 = document.createElement('img');
        img2.id = 'image';
        img2.src = pass;
        result2.innerHTML = '';
        result2.appendChild(img2)
        image_2 = pass
        cropper2 = new Cropper(img2, {
          zoomOnWheel: false,
          movable: false,
          guides: false,
          crop: function (co) {
            x12 = co.detail.x
            y12 = co.detail.y
            y22 = co.detail.height + co.detail.y
            x22 = co.detail.width + co.detail.x
          },
          cropend: function(e){
            sData()
          }
        });
      
    });
    reader.readAsDataURL(this.files[0]);
  
});

cb1.addEventListener('change',function(){
  sData()
})

cb2.addEventListener('change',function(){
  sData()
})

opt.addEventListener('change',  function(){
  sData()
})


submit.addEventListener('click', e => {
  e.preventDefault();
  sData()
}
)
